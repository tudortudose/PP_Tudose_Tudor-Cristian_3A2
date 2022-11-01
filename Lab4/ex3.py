import os.path


def get_last_lines_or_dir_files(path):
    try:
        if not (os.path.exists(path)):
            raise Exception("Path does not exist!")
        if os.path.isfile(path):
            return solve_file(path)
        elif os.path.isdir(path):
            return solve_dir(path)
    except Exception as e:
        print("Exception: " + str(e))


def solve_file(path):
    try:
        with open(path, 'rb') as f:
            f.seek(-20, 2)
            string = f.read().decode('utf-8')
            return string
    except Exception as e:
        print("Exception: " + str(e))


def solve_dir(path):
    try:
        dictionary = {}
        for (root, directories, files) in os.walk(path):
            for file in files:
                dictionary[get_file_extension(file)] = dictionary.setdefault(get_file_extension(file), 0) + 1
        my_list = list(dictionary.items())
        my_list.sort(key=lambda el: el[1])
        return my_list
    except Exception as e:
        print("Exception: " + str(e))


def get_file_extension(file):
    return os.path.splitext(file)[1][1:]
