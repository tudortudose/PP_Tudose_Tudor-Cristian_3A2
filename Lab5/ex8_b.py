def multiply_output(function):
    def f(*args, **kwargs):
        return function(*args, **kwargs) * 2
    return f


def multiply_by_three(x):
    return x * 3


augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
print(x)