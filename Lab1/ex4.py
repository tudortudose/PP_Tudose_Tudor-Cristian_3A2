def convertCamelToSnake(string):
    snake_string = ""

    for i in string:
        if 'A' < i < 'Z':
            snake_string += '_'
            snake_string += chr(ord(i) + 32)
        else:
            snake_string += i

    return snake_string[1:]
