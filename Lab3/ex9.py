def get_valid_positional_args(*args, **kwargs):
    s = set()
    counter = 0
    for arg in kwargs:
        s.add(kwargs[arg])
    for pos_arg in args:
        if pos_arg in s:
            counter += 1
    return counter
