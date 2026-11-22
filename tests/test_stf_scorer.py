import numpy as np
import pandas as pd
import pytest

torch = pytest.importorskip("torch")
transformers = pytest.importorskip("transformers")
from tokenizers import ByteLevelBPETokenizer
from transformers import RobertaConfig, RobertaModel, RobertaTokenizerFast

from stresstwin_p import score_texts as ST
from stresstwin_p.stf_scorer import STFEnsemble, TopBlock, load_ensemble


@pytest.fixture(scope="module")
def kit(tmp_path_factory):
    d = tmp_path_factory.mktemp("bb")
    corpus = ["I can't sleep and I feel overwhelmed by work.", "We went to the park and had a lovely picnic.",
              "The bus leaves at nine every morning."] * 30
    bt = ByteLevelBPETokenizer()
    bt.train_from_iterator(corpus, vocab_size=400, min_frequency=1, special_tokens=["<s>", "<pad>", "</s>", "<unk>", "<mask>"])
    bt.save_model(str(d))
    tok = RobertaTokenizerFast(vocab_file=str(d / "vocab.json"), merges_file=str(d / "merges.txt"))
    torch.manual_seed(0)
    cfg = RobertaConfig(vocab_size=400, hidden_size=768, num_hidden_layers=12, num_attention_heads=12, intermediate_size=3072,
                        max_position_embeddings=514, type_vocab_size=1, pad_token_id=1, bos_token_id=0, eos_token_id=2)
    bb = RobertaModel(cfg, add_pooling_layer=False).eval()
    bb.save_pretrained(str(d)); tok.save_pretrained(str(d))
    for s in range(2):
        torch.manual_seed(10 + s)
        tb = TopBlock(bb, 2)
        with torch.no_grad():
            tb.head.weight.normal_(0, 0.05)
        torch.save(tb.state_dict(), d / f"stresstwin_f_s{s}.pt")
    return d


TEXTS = ["I feel completely overwhelmed and cannot sleep.", "A calm lovely day at the park.", "x", "The report is due. " * 80]


def test_ensemble_shapes_seed_difference_and_equivalence_of_interfaces(kit):
    ens = load_ensemble(kit, kit, seeds=(0, 1), device="cpu")
    z = ens.multi_logits(TEXTS)
    assert z.shape == (2, 4) and np.isfinite(z).all() and np.abs(z[0] - z[1]).max() > 1e-4
    assert np.allclose(np.array([f(TEXTS) for f in ens.scorers()]), z)
    z2 = STFEnsemble(kit, [kit / "stresstwin_f_s0.pt", kit / "stresstwin_f_s1.pt"], device="cpu", batch_size=2).multi_logits(TEXTS)
    assert np.abs(z - z2).max() < 5e-3                                  # batch size / padding invariance


def test_missing_checkpoint_and_wrong_keys_fail_loudly(kit, tmp_path):
    with pytest.raises(FileNotFoundError):
        load_ensemble(kit, kit, seeds=(0, 7), device="cpu")
    bad = tmp_path / "bad.pt"
    torch.save({"head.weight": torch.zeros(1, 1536)}, bad)
    with pytest.raises(RuntimeError):
        STFEnsemble(kit, [bad], device="cpu")


def test_score_table_accepts_the_multi_seed_object(kit):
    ens = load_ensemble(kit, kit, seeds=(0, 1), device="cpu")
    texts = pd.DataFrame({"obs_id": ["a", "b"], "text": [TEXTS[0], TEXTS[3]]})
    out = ST.score_table(texts, ens, batch_size=1)
    z = ens.multi_logits(texts.text.tolist())
    assert np.allclose(out.z_mean, z.mean(0), atol=5e-3) and np.allclose(out.z_var, z.var(0, ddof=1), atol=5e-3)
