# Data

## Public sources

* **Reddit mental-health timelines** (anxiety, bipolar, depression, suicidewatch; 2017): Murai, Silveira Fraga and Couto da Silva, Zenodo, doi:10.5281/zenodo.4266616 (CC BY 4.0). Download the four community archives and keep them outside this repository.
* **Dreaddit**: Turcan and McKeown (2019), used only to train and evaluate the StressTwin-F scorer.

The Zenodo files are Python pickles. `stresstwin_p/safe_io.py` reads them through a restricted unpickler that accepts plain data types only; do not load them with `pickle.load`.

## Files produced by the pipeline

| File | Content | Shared here? |
|---|---|---|
| `observations.csv` | hashed author, community, time in days, kind, length, thread | No (regenerated) |
| `texts.csv` | post text, used only for scoring | **Never shared** |
| `salt.bin` | secret salt of the author hash | **Never shared** |
| `scores.csv` | StressTwin-F score `y`, seed variance, two half-text logits | No (regenerated) |
| `results/seedN/results.json`, `report.md` | aggregate LOCO results per partition seed | Yes |
| `records.csv.gz` (per seed, about 58 MB) | one row per scored test prediction (hashed author, time, score, prediction, variance) | Not in the repository; distributed separately (see below) |

## Per-prediction records

`reproduce/compute_values.py` needs the per-seed `records.csv.gz` files. They contain hashed author identifiers only. They are not stored in git because of their size; place them in the Zenodo or release archive accompanying the paper (`[record DOI to be added]`) and check them against `results/records_sha256.txt`. All paper values derived from them are already stored in `results/values.json` and `results/diagnostics.json`, so tables and figures can be regenerated without them.

## Privacy rules

No raw text, author name, salt or unhashed identifier may be committed. `.gitignore` excludes the known private file names.
