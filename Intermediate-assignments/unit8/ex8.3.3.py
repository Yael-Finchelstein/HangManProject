def count_chars(my_str):
    dict_char_count = {}
    for char in my_str:
        if char in dict_char_count:
            dict_char_count[char] += 1
        else:
            dict_char_count[char] = 1
    return dict_char_count
