"""Scorer for StressTwin-F exactly as defined in the stresstwin_f reproducibility package.

Model: frozen RoBERTa layers 1..10 (a backbone folder) -> trainable top-2 layers -> [CLS ; mean-pool] (1536)
       -> Linear(1536, 1) -> ONE stress logit  (positive = stress).
This is NOT a Hugging Face sequence-classification model, so score_texts.hf_scorers cannot load it. Use this.

Files needed (written by the retrain notebook):
    backbone_dir/                the frozen RoBERTa folder (config, weights, tokenizer)
    ckpt_dir/stresstwin_f_s{0..4}.pt   state dicts of the top block + head, one per seed

Equivalence with the original code path (cached layer-10 states, fp16-rounded, TopKClassifier) was checked
numerically; set mimic_fp16_cache=False to skip the fp16 rounding of layer-10 states (differences are about 1e-3 in logit).
"""
from __future__ import annotations

import copy
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from transformers import RobertaModel, RobertaTokenizerFast


class TopBlock(nn.Module):
    """Same attribute names as the package's TopKClassifier, so its state dicts load with strict=True."""

    def __init__(self, backbone, k: int = 2, dropout: float = 0.1):
        super().__init__()
        self.layers = nn.ModuleList([copy.deepcopy(l) for l in backbone.encoder.layer[-k:]])
        self.drop = nn.Dropout(dropout)
        self.head = nn.Linear(2 * 768, 1)

    def forward(self, h, mask):
        ext = (1.0 - mask[:, None, None, :].to(h.dtype)) * -1e9
        for l in self.layers:
            h = l(h, attention_mask=ext)[0]
        m = mask.unsqueeze(-1).to(h.dtype)
        mean = (h * m).sum(1) / m.sum(1)
        return self.head(self.drop(torch.cat([h[:, 0], mean], -1))).squeeze(-1)


class STFEnsemble:
    """All seeds share one pass through the frozen prefix. multi_logits(texts) -> array (n_seeds, n_texts)."""
    multi = True

    def __init__(self, backbone_dir, ckpt_paths, device: str | None = None, max_len: int = 256,
                 keep_layer: int = 10, k: int = 2, mimic_fp16_cache: bool = True, batch_size: int = 32):
        self.device = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))
        self.max_len, self.keep_layer, self.bs, self.mimic = max_len, keep_layer, batch_size, mimic_fp16_cache
        self.tok = RobertaTokenizerFast.from_pretrained(str(backbone_dir))
        full = RobertaModel.from_pretrained(str(backbone_dir), add_pooling_layer=False).eval()
        n_layers = len(full.encoder.layer)
        if keep_layer != n_layers - k:
            raise ValueError(f"keep_layer={keep_layer} must equal n_layers-k={n_layers - k}")
        tops = []
        for p in ckpt_paths:
            tb = TopBlock(full, k)
            tb.load_state_dict(torch.load(str(p), map_location="cpu", weights_only=True), strict=True)
            tops.append(tb.eval().to(self.device))
        full.encoder.layer = full.encoder.layer[:keep_layer]      # the prefix only; last_hidden_state == layer-10 output
        self.prefix = full.to(self.device)
        self.tops = tops
        self.n_seeds = len(tops)

    @torch.no_grad()
    def multi_logits(self, texts) -> np.ndarray:
        texts = [str(t) for t in texts]
        ids = self.tok(texts, truncation=True, max_length=self.max_len)["input_ids"]
        order = np.argsort([len(x) for x in ids])
        out = np.zeros((self.n_seeds, len(texts)), np.float64)
        for b in range(0, len(texts), self.bs):
            sel = order[b:b + self.bs]
            batch = self.tok.pad({"input_ids": [ids[i] for i in sel]}, return_tensors="pt").to(self.device)
            h = self.prefix(**batch).last_hidden_state
            if self.mimic:
                h = h.half().float()
            m = batch["attention_mask"]
            for s, top in enumerate(self.tops):
                out[s, sel] = top(h, m).float().cpu().numpy()
        return out

    def scorers(self):
        """One callable per seed (compatible with score_table's list interface; slower: repeats the prefix)."""
        return [(lambda xs, s=s: self.multi_logits(xs)[s]) for s in range(self.n_seeds)]


def load_ensemble(backbone_dir, ckpt_dir, name: str = "stresstwin_f", seeds=(0, 1, 2, 3, 4), **kw) -> STFEnsemble:
    paths = [Path(ckpt_dir) / f"{name}_s{s}.pt" for s in seeds]
    missing = [str(p) for p in paths if not p.exists()]
    if missing:
        raise FileNotFoundError("missing checkpoint files: " + ", ".join(missing))
    return STFEnsemble(backbone_dir, paths, **kw)
