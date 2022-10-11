def countWordsInString(string):
    string = string.lstrip().rstrip()  # removing left and rights spaces if there are any
    return string.count(' ') + 1
