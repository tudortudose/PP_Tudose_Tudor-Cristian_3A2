import os.path


def get_last_lines_or_dir_files(path):
    if not (os.path.exists(path)):
        raise Exception("path does not exist")
    if os.path.isfile(path):
        return solve_file(path)
    elif os.path.isdir(path):
        return solve_dir(path)


def solve_file(path):
    with open(path, 'r') as f:
        string = f.read()
        string = string[-20:]
        return string


def get_file_extension(file):
    return os.path.splitext(file)[1][1:]


def solve_dir(path):
    dictionary = {}
    for (root, directories, files) in os.walk(path):
        for file in files:
            dictionary[get_file_extension(file)] = dictionary.setdefault(get_file_extension(file), 0) + 1
    my_list = list(dictionary.items())
    my_list.sort(key=lambda el: el[1])

    return my_list
