def getMostCommonLetterInString(string):
    string = string.upper()
    freq = [0] * 100

    for c in string:
        if 'A' <= c <= 'Z':
            freq[ord(c)] += 1

    max_val = max(freq)
    max_val_index = freq.index(max_val)
    return chr(max_val_index), max_val
