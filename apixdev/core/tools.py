import json
import os

import requirements as req_tool
from packaging.specifiers import SpecifierSet


def text_to_list(data):
    res = data.split("\n")

    return list(filter(bool, map(str.strip, res)))


def deduplicate(items):
    return list(set(items))


def get_requirements_from_path(path):
    """Recursively extract all requirements from root path"""
    requirements = []

    for r, d, f in os.walk(path):
        for file in f:
            if file == "requirements.txt":
                with open(os.path.join(r, file)) as tmp:
                    requirements += tmp.readlines()

    requirements = list({e.strip() for e in requirements})

    return requirements


def filter_requirements(items):
    """Cleans and eliminates duplicate requirements"""
    requirements = "\n".join(deduplicate(items))

    reqs = {}
    res = []

    for item in req_tool.parse(requirements):
        # Dict used to merge packages by name
        reqs.setdefault(item.name, [])
        reqs[item.name] += [SpecifierSet("".join(specs)) for specs in item.specs]

    for name, specs in reqs.items():
        if not specs:
            res.append(name)
            continue

        # Sort specifiers and keep only last one
        # FIXME: Not perfect IMHO, errors possible, fix it !
        specs = sorted({*specs}, key=str)
        res.append("".join([name, str(specs[-1])]))

    return res


def list_to_text(items):
    return "\n\n".join(items)


def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def dict_merge(dct, merge_dct):
    """Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
    ``dct``.
    :param dct: dict onto which the merge is executed
    :param merge_dct: dct merged into dct
    :return: None
    """
    for k, v in merge_dct.items():
        if (
            k in dct and isinstance(dct[k], dict) and isinstance(merge_dct[k], dict)
        ):  # noqa
            dict_merge(dct[k], merge_dct[k])
        else:
            dct[k] = merge_dct[k]


def bytes_to_json(data):
    res = data.rstrip().decode("utf8").replace("'", '"').replace("\n", ",")
    res = "[" + res + "]"
    res = res.replace(",]", "]")
    json_data = json.loads(res)

    return json_data
