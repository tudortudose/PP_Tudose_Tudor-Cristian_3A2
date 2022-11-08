def get_numbers_from_list(input_list):
    ret_list = []
    for el in input_list:
        if type(el) == int or type(el) == float:
            ret_list += [el]
    return ret_list


print(get_numbers_from_list([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))