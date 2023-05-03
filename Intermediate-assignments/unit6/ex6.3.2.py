def longest(my_list):
    sorted_list = sorted(my_list, key=len)
    print(sorted_list)
    return sorted_list[-1]
