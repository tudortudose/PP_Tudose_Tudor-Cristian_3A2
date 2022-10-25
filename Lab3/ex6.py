def get_unique_not_unique(_list):
    visited = set()
    unique_set = set()
    not_unique_set = set()

    for el in _list:
        if el not in visited:
            visited.add(el)
            unique_set.add(el)
        else:
            not_unique_set.add(el)
            if el in unique_set:
                unique_set.remove(el)
    return len(unique_set), len(not_unique_set)
