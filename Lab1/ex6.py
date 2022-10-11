def verifyPalindrome(x):
    x_str = str(x)
    x_inverted_str = x_str[::-1]
    return x_str == x_inverted_str
