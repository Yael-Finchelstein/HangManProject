def shift_left(my_list):
    """
    The function gets a list and returns a new list shifted one step to the left
    :param my_list: a list of length 3
    :return: new list shifted one step to the left
    """
    first, second, third = my_list
    new_list = [second, third, first]
    return new_list
