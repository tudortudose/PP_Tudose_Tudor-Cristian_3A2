import os


def get_full_path_files(dir_name):
    files = [f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))]
    abs_paths = [os.path.join(dir_name, f) for f in files]
    return abs_paths