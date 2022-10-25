import json


def get_dictionary_difference(dict1_file, dict2_file, result_file):
    with open(dict1_file) as f:
        dict1 = json.load(f)
    with open(dict2_file) as f:
        dict2 = json.load(f)

    result = get_differences(dict1, dict2)
    print(result)
    with open(result_file, "w") as f:
        json.dump(result, f, indent=2)


def get_differences(el1, el2):
    if type(el1) != type(el2): return
    result = {}
    if type(el1) is list:
        return list(set(el1).symmetric_difference(set(el2)))
    elif type(el1) is dict:
        print("dict")
        for key, val1 in el1.items():
            if key in el2.keys():
                val2 = el2[key]
                diffs = get_differences(val1, val2)
                if len(diffs) > 0:
                    result[key] = diffs
            else:
                result[key] = val1

        for key, val2 in el2.items():
            if key not in el1.keys():
                result[key] = val2
        return result
    else:
        if el1 == el2:
            return []
        else:
            return [el1, el2]

