def process(**kwargs):
    fib_nums = generate_fibonacci_seq(1000)
    if "filters" in kwargs.keys():
        for filter_func in kwargs.get("filters"):
            fib_nums = [x for x in fib_nums if filter_func(x)]
    if "offset" in kwargs.keys():
        fib_nums = fib_nums[kwargs.get("offset"):]
    if "limit" in kwargs.keys():
        fib_nums = fib_nums[:kwargs.get("limit")]
    return fib_nums

def generate_fibonacci_seq(n):
    fib = []
    for i in range(n):
        if i == 0 or i == 1:
            fib += [i]
        else:
            fib += [fib[i-1]+fib[i-2]]
    return fib


def sum_digits(x):
    return sum(map(int, str(x)))


print(process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],

    limit=2,

    offset=2
))