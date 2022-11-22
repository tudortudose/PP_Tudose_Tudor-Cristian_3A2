import re

def get_words(string):
    return re.findall(r"[a-zA-Z]+[a-zA-Z1-9]*", string)


# example
print(get_words("lkk var123, kdsal, ds54 123"))
