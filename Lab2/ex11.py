def orderTupleLists(tupleList):
    tupleList.sort(key=lambda tup: tup[1][2])
    return tupleList
