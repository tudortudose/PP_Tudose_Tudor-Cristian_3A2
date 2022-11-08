def sum_elements(*args, **kwargs):
    s = 0
    for arg in kwargs.values():
        s += arg
    return s


sum_lambda = lambda *args, **kwargs: sum(kwargs.values())


print(sum_elements(1, 2, b=1, c=3))
print(sum_lambda(1, 2, b=1, c=3))
