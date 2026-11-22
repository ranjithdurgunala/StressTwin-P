"""Check that the exported weights reproduce the logits the training run stored (run AFTER the retrain notebook).

usage (from the repro package folder, using the venv python):
    python verify_export.py --backbone artifacts/roberta_backbone --ckpt_dir results/ckpt --name stresstwin_f

It scores 200 official-test posts with the stresstwin_p scorer and compares with results/preds/<name>_s<seed>.csv.
PASS: max abs logit difference below 5e-3 for every seed.
"""
import argparse, sys
import numpy as np, pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("--backbone", required=True); ap.add_argument("--ckpt_dir", required=True)
ap.add_argument("--name", default="stresstwin_f"); ap.add_argument("--n", type=int, default=200)
ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2, 3, 4])
ap.add_argument("--stresstwin_p_path", default=None, help="folder that contains the stresstwin_p package (if not pip-installed)")
a = ap.parse_args()
if a.stresstwin_p_path:
    sys.path.insert(0, a.stresstwin_p_path)
from stresstwin_p.stf_scorer import load_ensemble

allp = pd.read_csv("cache/all_posts.csv")
te = allp[allp.split0 == "test"].head(a.n)
ens = load_ensemble(a.backbone, a.ckpt_dir, name=a.name, seeds=tuple(a.seeds))
z = ens.multi_logits(te.text.tolist())
ok = True
for k, s in enumerate(a.seeds):
    pr = pd.read_csv(f"results/preds/{a.name}_s{s}.csv").set_index("uid").loc[te.uid, "logit"].to_numpy()
    d = float(np.abs(z[k] - pr).max())
    print(f"seed {s}: max |logit diff| = {d:.5f}", "PASS" if d < 5e-3 else "FAIL")
    ok &= d < 5e-3
print("ALL PASS" if ok else "CHECK FAILED - do not use these weights; send me this output")
sys.exit(0 if ok else 1)
