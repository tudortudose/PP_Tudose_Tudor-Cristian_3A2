def getNFibonacciNumbers(n):
    fib_list = []
    for i in range(n):
        if i == 0 or i == 1:
            fib_list += [i]
        else:
            fib_list += [(fib_list[i - 1] + fib_list[i - 2])]
    return fib_list
