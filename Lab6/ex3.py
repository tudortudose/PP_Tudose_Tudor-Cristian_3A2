import re


def get_matched_substrings(input_string, regexes):
    match_set = set()
    for regex in regexes:
        matches = re.findall(regex, input_string)
        for match in matches:
            match_set.add(match)
    return match_set


# example
print(get_matched_substrings("salut 123 hello, yey", [
    r'[1-9]+',
    r'[a-z]+',
]))
