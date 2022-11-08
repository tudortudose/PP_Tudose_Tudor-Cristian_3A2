def process_item(x):
    x += 1
    while not (is_prime(x)):
        x += 1
    return x


def is_prime(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


input_int = int(input("Input a number:"))
print(f"Least prime greater than {input_int} is: ", process_item(input_int))
