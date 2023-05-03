def sequence_del(my_str):
    result = ""
    prev_char = ""
    for char in my_str:
        if char != prev_char:
            result += char
            prev_char = char
    return result
