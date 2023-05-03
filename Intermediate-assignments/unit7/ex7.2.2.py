def numbers_letters_count(my_str):
    numbers, letters = 0, 0
    for letter in my_str:
        if letter.isdigit():
            numbers += 1
        elif letter.isalpha() or letter.isascii():
            letters += 1
    list = [numbers, letters]
    return list
