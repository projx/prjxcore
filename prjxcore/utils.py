from prjxcore.AppLog import *
from pprint import pprint
from copy import deepcopy

### A dumping ground for some useful functions I use in other projects
def merge_nested_dicts(a: dict, b: dict) -> dict:
    result = deepcopy(a)
    for bk, bv in b.items():
        av = result.get(bk)
        if isinstance(av, dict) and isinstance(bv, dict):
            result[bk] = merge_nested_dicts(av, bv)
        else:
            result[bk] = deepcopy(bv)
    return result