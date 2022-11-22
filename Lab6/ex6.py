import re


def censor_text(text):
    words = re.findall(r"[a-zA-Z]+", text)
    matches = []
    for word in words:
        if re.match(r'[aeiou]+[a-zA-Z]*[aeiou]+$', word):
            matches += [word]

    for match in matches:
        replace_string = match
        for index, ch in enumerate(replace_string):
            if index % 2 == 0:
                replace_string = replace_string[:index] + '*' + replace_string[index+1:]
        expression = r'{}'.format(match)
        text = re.sub(expression, replace_string, text)
    return text


# example
print(censor_text("ana are mere iar eu nu am abcde"))
