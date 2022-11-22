import os
import re


def rec_scroll(directory, regex):
    for (root, directories, files) in os.walk(directory):
        for fileName in files:
            with open(os.path.join(directory, fileName), 'r') as f:
                file_text = f.read()
            name_match = re.match(regex, fileName)
            text_match = re.match(regex, file_text)
            if name_match and text_match:
                print(">>", fileName)
            elif name_match or text_match:
                print(fileName)


# example
rec_scroll("test_dir", r'.*file.*')