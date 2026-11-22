#!/usr/bin/env python
"""Fine-tune the top-k RoBERTa block (plain vs fidelity-aware), then run the audit.

usage: 03_train_eval.py --name plain_ft --seeds 0 1 2 3 4 [--fidelity --lam_cc 1 --lam_st 1]
Writes results/runs/<name>_s<seed>.json and results/preds/<name>_s<seed>.csv
(logits for original + every audit view on the test rows, and val/train rows).
"""
import argparse, json, os, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import numpy as np, torch
from stresstwin import protocol as P, encode as E, models as Mo, fidelity as F, perturb as PT, metrics as M

ap = argparse.ArgumentParser()
ap.add_argument("--name", required=True); ap.add_argument("--seeds", type=int, nargs="+", default=[0])
ap.add_argument("--k", type=int, default=2); ap.add_argument("--epochs", type=int, default=4)
ap.add_argument("--lr", type=float, default=3e-5); ap.add_argument("--bs", type=int, default=16)
ap.add_argument("--fidelity", action="store_true")
ap.add_argument("--lam_cc", type=float, default=1.0); ap.add_argument("--lam_st", type=float, default=1.0)
ap.add_argument("--margin", type=float, default=0.25)
ap.add_argument("--no_audit", action="store_true", help="tuning mode: skip test-pool audit (validation only)")
ap.add_argument("--threads", type=int, default=2)
ap.add_argument("--ckpt_dir", default=None,
                help="if set, save the trained top block + head to <ckpt_dir>/<name>_s<seed>.pt (needed by stresstwin_p)")
a = ap.parse_args()
torch.set_num_threads(a.threads)
log = lambda s: print(time.strftime("%H:%M:%S"), s, flush=True)
os.makedirs("results/runs", exist_ok=True)

pr = P.load_protocol(); y = pr["y"]; tr, va, te = pr["tr_idx"], pr["va_idx"], pr["te_idx"]
_, bb = E.load_backbone()
c0 = E.load_cache("cache/orig.npz")
n_tr_rows = int((pr["allp"].split0 == "train").sum())       # train-pool views cover official-train rows only
views = {v: E.load_cache(f"cache/trainview_{v}.npz") for v in PT.TRAIN_VIEWS}
te_off = n_tr_rows
masks = dict(np.load("results/audit_masks.npz")) if not a.no_audit else {}

for seed in a.seeds:
    out = f"results/runs/{a.name}_s{seed}.json"
    ck = os.path.join(a.ckpt_dir, f"{a.name}_s{seed}.pt") if a.ckpt_dir else None
    if (os.path.exists(ck) if ck else os.path.exists(out)):     # with --ckpt_dir a seed counts as done only if its weights exist
        log(f"skip {ck or out}"); continue
    log(f"=== {a.name} seed={seed} fidelity={a.fidelity}")
    cfg = Mo.TrainCfg(k=a.k, epochs=a.epochs, lr=a.lr, bs=a.bs, fidelity=a.fidelity, lam_cc=a.lam_cc,
                      lam_st=a.lam_st, margin=a.margin, seed=seed)
    # train-view caches are indexed by official-train row == uid (train rows come first)
    model, info = Mo.train_model(bb, c0, views, tr, y, va, cfg, logf=log)
    if ck:
        os.makedirs(a.ckpt_dir, exist_ok=True)
        torch.save(model.state_dict(), ck + ".tmp"); os.replace(ck + ".tmp", ck)      # atomic: a half-written file never counts
        log(f"saved weights {ck}")
    z_all = np.full(len(y), np.nan)
    z_all[va] = Mo.predict_logits(model, c0, va); z_all[tr] = Mo.predict_logits(model, c0, tr)
    if not a.no_audit:
        z_all[te] = Mo.predict_logits(model, c0, te)
    rec = {"name": a.name, "seed": seed, "cfg": vars(a), "info": info}
    if not a.no_audit:   # tuning mode never touches the test set
        rec["test"] = P.evaluate_scores(pr, z_all[va], z_all[te])
    # validation-only fidelity on TRAIN-pool templates (used for tuning lam, never test-pool)
    zs = {v: Mo.predict_logits(model, views[v], va) for v in PT.TRAIN_VIEWS}
    rec["val_fidelity_trainpool"] = {**F.counterfactual_consistency(z_all[va], zs["stress_ins"], zs["relief_ins"]),
                                     **F.stability(z_all[va], zs["neutral_ins"])}
    if not a.no_audit:
        audit = {v: E.load_cache(f"cache/auditview_{v}.npz") for v in PT.AUDIT_VIEWS}   # loaded after training (memory)
        zt = z_all[te]; zv = {}
        for v in PT.AUDIT_VIEWS:
            zv[v] = Mo.predict_logits(model, audit[v], np.arange(len(te)))
        rec["audit"] = {
            **F.counterfactual_consistency(zt, zv["stress_ins"], zv["relief_ins"]),
            "st_neutral": F.stability(zt, zv["neutral_ins"]),
            "st_surface": F.stability(zt, zv["surface"]),
            "neg_del": F.directional(zt, zv["neg_del"], "down", masks["neg_del"]),
        }
        P.save_preds(f"{a.name}_s{seed}", pr, z_all)
        np.savez(f"results/preds/{a.name}_s{seed}_views.npz", orig=zt, **{k: v for k, v in zv.items()})
    json.dump(rec, open(out, "w"), indent=1, default=float)
    if a.no_audit:
        vf = rec["val_fidelity_trainpool"]
        log(f"[val only] best_epoch={info['best_epoch']} val_nll={min(h['val_nll'] for h in info['history']):.4f} "
            f"val CC={vf['cc_dir']:.3f} ST|dp|={vf['st_mean_abs_dp']:.4f}")
    else:
        log(f"F1={rec['test']['f1']:.4f} AUROC={rec['test']['auroc']:.4f} ECE={rec['test']['ece']:.4f} "
            f"CC={rec['audit']['cc_dir']:.3f} ST|dp|={rec['audit']['st_neutral']['st_mean_abs_dp']:.4f}")
