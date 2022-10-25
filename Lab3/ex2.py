def get_chr_occurrence(string):
    dictionary = {}
    for ch in string:
        dictionary[ch] = dictionary.setdefault(ch, 0) + 1
    return dictionary
