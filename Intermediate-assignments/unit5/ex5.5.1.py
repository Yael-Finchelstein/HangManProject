def is_valid_input(letter_guessed):
    """
    The function checks if the parameter is valid
    :param letter_guessed: a string that represents the guess
    :return: boolean: True if the param is valid and False otherwise
    """
    if len(letter_guessed) == 1 and letter_guessed.isalpha():
        return True
    elif len(letter_guessed) > 1 or letter_guessed.isascii():
        return False
