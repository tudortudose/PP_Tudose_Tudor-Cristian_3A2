def getPrimeNumbersInList(_list):
    return list(filter(isPrime, _list))


def isPrime(num):
    if num == 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True
