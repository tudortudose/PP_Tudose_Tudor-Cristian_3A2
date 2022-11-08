def get_dicts(*args, **kwargs):
    ret_list = []
    for arg in args:
        if verify_dict(arg):
            ret_list += [arg]

    for arg in kwargs.values():
        if verify_dict(arg):
            ret_list += [arg]

    return ret_list


def verify_dict(arg):
    if type(arg) != dict:
        return False
    if len(arg.keys()) < 2:
        return False
    ok = False
    for key in arg.keys():
        if type(key) == str and len(key) >= 3:
            ok = True
    return ok


print(get_dicts(
    {1: 2, 3: 4, 5: 6},

    {'a': 5, 'b': 7, 'c': 'e'},

    {2: 3},

    [1, 2, 3],

    {'abc': 4, 'def': 5},

    3764,

    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

    test={1: 1, 'test': True}
))