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


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries + 1])
