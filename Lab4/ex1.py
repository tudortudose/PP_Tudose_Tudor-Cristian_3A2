import os


def get_file_extensions(director):
    try:
        files = [f for f in os.listdir(director) if os.path.isfile(os.path.join(director, f))]
        extensions = [os.path.splitext(file)[1][1:] for file in files]
        extensions = list(set(extensions))
        extensions.sort()
        return extensions
    except Exception as e:
        print("Exception: " + str(e))
