from ex8_a import print_arguments
from ex8_b import multiply_output


def augment_function(function, decorators):
    for func in decorators:
        function = func(function)

    def f(*args, **kwargs):
        return function(*args, **kwargs)

    return f


def add_numbers(a, b):
    return a + b


decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
print(x)
