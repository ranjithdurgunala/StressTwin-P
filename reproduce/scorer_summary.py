"""Summarise the scorer retraining log: F1, counterfactual consistency (CC) and stability (ST) per model.

    python reproduce/scorer_summary.py results/scorer_retrain_log.txt
"""
import re, statistics as st, sys
from collections import defaultdict

def main(path):
    rows, cur = defaultdict(list), None
    for line in open(path):
        m = re.search(r"=== (\w+) seed=(\d+)", line)
        if m:
            cur = m.group(1); continue
        m = re.search(r"F1=([\d.]+).*CC=([\d.]+)\s+ST\|dp\|=([\d.]+)", line)
        if m and cur:
            rows[cur].append(tuple(map(float, m.groups())))
    for name, v in rows.items():
        f1, cc, s = zip(*v)
        print(f"{name:14s} seeds={len(v)} F1 {st.mean(f1):.3f} (SD {st.stdev(f1):.3f})  CC {st.mean(cc):.3f}  ST {st.mean(s):.3f}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "results/scorer_retrain_log.txt")
