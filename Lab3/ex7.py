from ex1 import get_sets_from_lists


def get_relations(*sets):
    relations = dict()
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            current_relations = get_sets_from_lists(sets[i], sets[j])
            relations[repr(sets[i]) + " | " + repr(sets[j])] = current_relations[0]
            relations[repr(sets[i]) + " & " + repr(sets[j])] = current_relations[1]
            relations[repr(sets[i]) + " - " + repr(sets[j])] = current_relations[2]
            relations[repr(sets[j]) + " - " + repr(sets[i])] = current_relations[3]
    return relations
