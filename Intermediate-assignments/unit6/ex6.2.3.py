def format_list(my_list):
    even_elements = my_list[::2]
    last_element = my_list[-1]
    formatted_str = ", ".join(even_elements) + " and " + last_element
    return formatted_str
