import os


def write_file_paths(director, fisier):
    files = [f for f in os.listdir(director) if f.startswith("A")]
    with open(fisier, 'w') as result_file:
        for file in files:
            result_file.write(os.path.abspath(director) + "\\" + file + '\n')