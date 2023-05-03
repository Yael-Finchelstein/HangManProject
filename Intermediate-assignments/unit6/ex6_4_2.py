from ex6_4_1 import check_valid_input


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        sorted_letters = sorted(old_letters_guessed, key=str.lower)
        separator = ' -> '
        formatted_str = separator.join(sorted_letters).lower()
        print(formatted_str)
        return False
