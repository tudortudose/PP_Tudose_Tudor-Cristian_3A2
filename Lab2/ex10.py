def getTransposedLists(*lists):
    max_len = max(len(x) for x in lists)
    new_lists = [[] for x in range(max_len)]
    for i in range(max_len):
        for _list in lists:
            if (len(_list)) <= i:
                new_lists[i] += [None]
            else:
                new_lists[i] += [_list[i]]
    return new_lists
