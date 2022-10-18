def getCharsFromStrings(strings, x=1, flag=True):
    chars = [[] for i in range(len(strings))]
    for idx, string in enumerate(strings):
        for c in string:
            if ord(c) % x == int(flag):
                chars[idx] += [c]
    return chars
