import os


def search_in_target(target, to_search):
    try:
        if not (os.path.exists(target)):
            raise Exception("Path does not exist!")
        if os.path.isfile(target):
            return solve_file(target, to_search)
        elif os.path.isdir(target):
            return solve_dir(target, to_search)
        else:
            raise ValueError("Target should be a file or a directory!")
    except Exception as e:
        print("Exception: " + str(e))


def search_file(target, to_search):
    try:
        with open(target, 'r') as f:
            string = f.read()
            return string.count(to_search) > 0
    except Exception as e:
        print("Exception: " + str(e))


def solve_file(target, to_search):
    try:
        if search_file(target, to_search):
            return target
        else:
            return None
    except Exception as e:
        print("Exception: " + str(e))


def solve_dir(target, to_search):
    try:
        valid_files = set()
        for (root, directories, files) in os.walk(target):
            for file in files:
                file_path = os.path.join(root, file)
                if search_file(file_path, to_search):
                    valid_files.add(file_path)
        return valid_files
    except Exception as e:
        print("Exception: " + str(e))
