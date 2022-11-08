def get_dicts(pairs):
    dict_list = []
    for pair in pairs:
        dict_list += [
            {
                'sum': pair[0] + pair[1],
                'prod': pair[0] * pair[1],
                'pow': pow(pair[0], pair[1])
            }
        ]
    return dict_list


print(get_dicts([(5, 2), (19, 1), (30, 6), (2, 2)]))
