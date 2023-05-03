def arrow(my_char, max_length):
    arrow_str = ''
    for i in range(1, max_length + 1):
        arrow_str += str(my_char * i)
        arrow_str += '\n'
        if i == max_length:
            for j in range(i - 1, 0, -1):
                arrow_str += str(my_char * j)
                arrow_str += '\n'
    return arrow_str
