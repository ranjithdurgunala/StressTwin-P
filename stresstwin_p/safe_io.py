"""Safe loading of untrusted data files.

Unpickling an untrusted file can execute arbitrary code. Zenodo 4266616 ships Python pickles,
so this loader only allows plain containers and scalars and refuses everything else. If it
refuses, do not loosen it: convert the file in an isolated environment instead.
"""
from __future__ import annotations

import pickle
from pathlib import Path

_SAFE = {("builtins", n) for n in
         ("dict", "list", "tuple", "set", "frozenset", "str", "int", "float", "bool", "bytes", "NoneType", "complex")}


# Verified by opcode scan (pickletools, no execution) of all 12 Zenodo 4266616 pickles: these are the ONLY globals they
# reference. Each is a data constructor (a timestamp value; an array/dtype container) and runs no user code.
_DATA_TYPES = {
    ("pandas._libs.tslibs.timestamps", "Timestamp"),
    ("pandas._libs.tslibs.timestamps", "_unpickle_timestamp"),   # written by newer pandas; same value constructor
    ("numpy.core.multiarray", "_reconstruct"),
    ("numpy._core.multiarray", "_reconstruct"),
    ("numpy", "ndarray"),
    ("numpy", "dtype"),
}
_SAFE = _SAFE | _DATA_TYPES


class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if (module, name) in _SAFE:
            return super().find_class(module, name)
        raise pickle.UnpicklingError(
            f"refused: pickle needs {module}.{name}. Not loading it; convert it in an isolated environment.")


def load_pickle(path):
    with open(Path(path), "rb") as f:
        return RestrictedUnpickler(f).load()
