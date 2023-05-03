def last_early(my_str):
    my_str = my_str.lower()
    last_char = my_str[-1]
    if last_char in my_str[:-1]:
        return True
    else:
        return False
