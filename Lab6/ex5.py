import re


def get_xml_elements(file, attrs):
    with open(file, 'r') as f:
        file_text = f.read()
    items = re.findall(r'<.*>', file_text)
    found_items = []
    for item in items:
        for key, value in attrs.items():
            expression = r'.*{}.*'.format(key + "=\"" + value + "\"")
            if re.match(expression, item):
                found_items += [item]
                break
    return found_items


# example
print(get_xml_elements('example.xlm',
                       {"class": "url", "name": "url-form", "data-id": "item"}))
