HANGMAN_ASCII_ART = """Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/\n"""

MAX_TRIES = 6

HANGMAN_PHOTOS = {
    1: "\tx-------x\n",
    2: "\tx-------x\n\t|\n\t|\n\t|\n\t|\n\t|\n",
    3: "\tx-------x\n\t|\t\t|\n\t|\t\t0\n\t|\n\t|\n\t|\n",
    4: "\tx-------x\n\t|\t\t|\n\t|\t\t0\n\t|\t\t|\n\t|\n\t|\n",
    5: r"""    x-------x
    |       |
    |       0
    |      /|\
    |
    |
""",
    6: r"""    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
""",
    7: r"""    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
"""}


def print_opening_screen():
    """
    The function prints the opening screen of the hangman game
    :return: None
    """
    print(HANGMAN_ASCII_ART, MAX_TRIES)


def check_win(secret_word, old_letters_guessed):
    """
    A function that checks whether the player was able to guess the secret word and thus won the game
    :param secret_word: A string that represents the secret word that the player has to guess
    :param old_letters_guessed: A list that contains the letters the player has guessed so far
    :return: The function returns True if all the letters that make up the secret word are included in
        the list of letters that the user guessed. Otherwise, the function returns False.
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """
    The function shows the player his progress in guessing the secret word
    :param secret_word: A string that represents the secret word that the player has to guess
    :param old_letters_guessed: A list that contains the letters the player has guessed so far
    :return: The function returns a string consisting of letters and underscores. The string shows the letters
        from the old_letters_guessed list that are in the secret_word string in their appropriate position, and the other letters in the string (which the player has not yet guessed) as underlines
    """
    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "
    return hidden_word.strip()


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    The function checks if the parameter is valid and whether the user has already guessed the character before
    :param letter_guessed: A string that represents the guess
    :param old_letters_guessed: A list that represents the old guesses
    :return: boolean: True if the param is valid and False otherwise
    """
    if len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed:
        return True
    elif len(letter_guessed) > 1 or letter_guessed.isascii() or letter_guessed.lower() in old_letters_guessed:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    A function that adds a character to the list of guesses, or prints a message if it cannot be added
    :param letter_guessed: A string that represents the character received from the player
    :param old_letters_guessed: A list that contains the letters the player has guessed so far
    :return: True if the addition was successful, or False which means that it is not possible to add the
        character to the list of already guessed characters.
    """
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


def choose_word(file_path, index):
    """
    The function selects for the player a word that will be the secret word for guessing, from a text
        file containing a list of words separated by spaces
    :param file_path: A string (file_path) representing a path to the text file
    :param index: An integer (index) representing the position of a certain word in the file.
    :return: A tuple consisting of two members: the number of different words in the file, and a word in the position
        received as an argument to the function (index), which will be used as the secret word for guessing.
    """
    with open(file_path, 'r') as file:
        words = file.read().split()
        unique_words = set(words)
        num_unique_words = len(unique_words)
        num_words = len(words)
        word_index = (index - 1) % num_words
        secret_word = words[word_index]
    return num_unique_words, secret_word


def print_hangman(num_of_tries):
    """
    The function prints one of the seven states of the hanging man
    :param num_of_tries: int that represents the number of failed attempts by the user so far
    :return: None
    """
    print(HANGMAN_PHOTOS[num_of_tries + 1])


def main():
    old_letter_guessed = []  # The letters the user has guessed so far
    num_of_tries = 0  # The current number of failed attempts

    print_opening_screen()

    # Ask the user for the path to the file, and keep asking until a valid path is entered
    while True:
        path = input("Please enter words file path: ")
        try:
            with open(path, 'r') as file:
                break
        except FileNotFoundError:
            print("File not found, please try again.")
    index = int(input("Please enter index for a word in the words file: "))
    print("\nLet’s start!")

    # Choose a secret word from the file based on the user's input
    secret_word = choose_word(path, index)[1]
    # Print the hangman and the hidden word
    print_hangman(0)
    print(show_hidden_word(secret_word, old_letter_guessed))

    # Keep asking for guesses until the player wins or loses
    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letter_guessed):
        letter = input("Please enter your guess: ")
        trying = try_update_letter_guessed(letter, old_letter_guessed)
        while not trying:
            letter = input("Please enter your guess: ")
            trying = try_update_letter_guessed(letter, old_letter_guessed)

        if letter.lower() in secret_word:
            print(show_hidden_word(secret_word, old_letter_guessed))
        else:
            num_of_tries += 1
            print(":(")
            print_hangman(num_of_tries)
            print(show_hidden_word(secret_word, old_letter_guessed))

    # Print the result (win/lose)
    if check_win(secret_word, old_letter_guessed):
        print("WIN")
    else:
        print("LOSE")


if __name__ == '__main__':
    main()
