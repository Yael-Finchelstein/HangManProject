def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    return sorted(list1) == sorted(list2)
