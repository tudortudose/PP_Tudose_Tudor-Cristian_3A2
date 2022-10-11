def count1BitsInNumber(number):
    binary_str = str(bin(number))
    return binary_str.count('1')
