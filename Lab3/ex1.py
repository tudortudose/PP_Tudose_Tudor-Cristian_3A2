def get_sets_from_lists(a, b):
    a = set(a)
    b = set(b)
    union = a.union(b)
    intersection = a.intersection(b)
    a_minus_b = a.difference(b)
    b_minus_a = b.difference(a)
    return [union, intersection, a_minus_b, b_minus_a]
