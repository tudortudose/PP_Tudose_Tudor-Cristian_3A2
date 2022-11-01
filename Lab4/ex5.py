import os


def search_in_target(target, to_search):
    if not (os.path.exists(target)):
        raise Exception("Path does not exist!")
    if os.path.isfile(target):
        return solve_file(target, to_search)
    elif os.path.isdir(target):
        return solve_dir(target, to_search)
    else:
        raise ValueError("Target should be a file or a directory!")


def search_file(target, to_search):
    with open(target, 'r') as f:
        string = f.read()
        return string.count(to_search) > 0


def solve_file(target, to_search):
    if search_file(target, to_search):
        return target
    else:
        return None


def solve_dir(target, to_search):
    valid_files = set()
    for (root, directories, files) in os.walk(target):
        for file in files:
            file_path = os.path.join(root, file)
            if search_file(file_path, to_search):
                valid_files.add(file_path)
    return valid_files
