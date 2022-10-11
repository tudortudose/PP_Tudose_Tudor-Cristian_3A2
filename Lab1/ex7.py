import re


# using regular expressions
def findFirstNumberInStringShortV(string):
    return re.search(r'\d+', string).group()


# without regular expressions
def findFirstNumberInStringLongV(string):
    started = False
    num_string = ""

    for i in string:
        if '0' <= i <= '9':
            num_string += i
            if not started:
                started = True
        else:
            if started:
                return num_string

    return num_string
