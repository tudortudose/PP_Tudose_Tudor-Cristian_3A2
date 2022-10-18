def getPalindromeCountAndGreatest(_list):
    palindromes = []
    for num in _list:
        if isPalindrome(num):
            palindromes += [num]
    return palindromes, max(palindromes)


def isPalindrome(num):
    return str(num) == str(num)[::-1]
