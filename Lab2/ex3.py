def getListSets(list1, list2):
    intersection = [val for val in list1 if val in list2]
    reunion = list(set().union(list1, list2))
    l1_minus_l2 = [val for val in list1 if val not in list2]
    l2_minus_l1 = [val for val in list2 if val not in list1]
    return intersection, reunion, l1_minus_l2, l2_minus_l1
