def getItemsFromLists(*lists, x):
    dictionary = {}
    found_items = []
    for l in lists:
        for el in l:
            if el in dictionary:
                dictionary[el] += 1
            else:
                dictionary[el] = 1
    for item in dictionary:
        if dictionary[item] == 2:
            found_items += [item]
    return found_items
