def check_valid_input(letter_guessed, old_letters_guessed):
    """
    The function checks if the parameter is valid and whether the user has already guessed the character before
    :param letter_guessed: a string that represents the guess
    :param old_letters_guessed: a list that represents the old guesses
    :return: boolean: True if the param is valid and False otherwise
    """
    if len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed:
        return True
    elif len(letter_guessed) > 1 or letter_guessed.isascii() or letter_guessed.lower() in old_letters_guessed:
        return False
