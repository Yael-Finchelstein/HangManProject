def inverse_dict(my_dict):
    result_dict = {}
    for key, value in my_dict.items():
        if value in result_dict:
            result_dict[value].append(key)
        else:
            result_dict[value] = [key]
    for value in result_dict.values():
        value.sort()
    return result_dict
