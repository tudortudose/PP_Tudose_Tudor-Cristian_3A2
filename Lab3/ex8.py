def get_dict_loop(_dict):
    s = set()
    visit_order = []
    current = 'start'
    while _dict[current] not in s:
        current = _dict[current]
        s.add(current)
        visit_order.append(current)
    return visit_order
