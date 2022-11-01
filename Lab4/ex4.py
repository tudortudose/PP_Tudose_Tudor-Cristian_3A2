import os

from ex3 import get_file_extension


def get_non_empty_file_extensions(dir_name):
    try:
        files = [f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))]
        extensions = [get_file_extension(file) for file in files if get_file_extension(file) != ""]
        extensions = list(set(extensions))
        extensions.sort()
        return extensions
    except Exception as e:
        print("Exception: " + str(e))
