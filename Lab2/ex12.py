def makeRhymes(words):
    dictionary = {}
    for word in words:
        suf = word[-2:]
        if suf in dictionary:
            dictionary[suf] += [word]
        else:
            dictionary[suf] = [word]
    return dictionary
