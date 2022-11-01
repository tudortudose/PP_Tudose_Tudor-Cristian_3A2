import os.path
from ex3 import get_file_extension


def get_file_info(file_name):
    try:
        return {
            'full_path': os.path.abspath(file_name),
            'file_size': os.stat(file_name).st_size,
            'file_extension': get_file_extension(file_name),
            'can_read': os.access(file_name, os.R_OK),
            'can_write': os.access(file_name, os.W_OK)
        }
    except Exception as e:
        print("Exception: " + str(e))
