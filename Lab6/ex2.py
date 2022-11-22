import re


def get_matches(r_string, input_string, size):
    matches = re.findall(r_string, input_string)
    return list(filter(lambda x: len(x) == size, matches))


# example
print(get_matches(r'[1-9]+', 'salut 1233d dsaj123 dsain321', 3))
