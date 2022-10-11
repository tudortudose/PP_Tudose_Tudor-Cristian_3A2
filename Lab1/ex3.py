# using count
def countSubstringInStringAppearancesShortV(substring, string):
    return string.count(substring)


# without count
def countSubstringInStringAppearancesLongV(substring, string):
    counter = 0
    for i in range(len(string)):
        if stringStartsWithSubstring(string[i:], substring):
            counter += 1

    return counter


def stringStartsWithSubstring(string, substring):
    if len(string) < len(substring): return False
    for i in range(len(substring)):
        if substring[i] != string[i]:
            return False

    return True
