def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        words = file.read().split()
        unique_words = set(words)
        num_unique_words = len(unique_words)
        num_words = len(words)
        word_index = (index - 1) % num_words
        secret_word = words[word_index]
    return num_unique_words, secret_word
