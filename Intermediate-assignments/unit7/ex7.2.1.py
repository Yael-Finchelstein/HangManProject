def is_greater(my_list, n):
    new_list = []
    for number in my_list:
        if number > n:
            new_list.append(number)
    return new_list
