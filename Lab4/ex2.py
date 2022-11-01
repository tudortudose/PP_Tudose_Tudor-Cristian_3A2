import os


def write_file_paths(director, fisier):
    try:
        files = [f for f in os.listdir(director) if os.path.isfile(os.path.join(director, f)) and f.startswith("A")]
        with open(fisier, 'w') as result_file:
            for file in files:
                result_file.write(os.path.abspath(director) + "\\" + file + '\n')
    except Exception as e:
        print("Exception: " + str(e))
