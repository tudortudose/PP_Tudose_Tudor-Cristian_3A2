def find2GCD(a, b):
    if b == 0:
        return a
    return find2GCD(b, a % b)


def findGCD():
    gcd = int(input("Enter a number: "))

    while 1:
        y = input("Enter a number: ")
        if y == "":
            break
        y = int(y)
        gcd = find2GCD(y, gcd)

    return gcd
