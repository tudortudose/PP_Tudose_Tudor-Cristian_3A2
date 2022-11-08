def get_odd_even_tuples(input_list):
    even_list = []
    odd_list = []
    for el in input_list:
        if el % 2 == 0:
            even_list += [el]
        else:
            odd_list += [el]

    tuples = []
    for i in range(len(even_list)):
        tuples += [(even_list[i], odd_list[i])]

    return tuples


print(get_odd_even_tuples([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))