def get_unique_not_unique(_list):
    s = {}
    unique_count = 0
    for i in _list:
        if i not in s:
            unique_count += 1
            
