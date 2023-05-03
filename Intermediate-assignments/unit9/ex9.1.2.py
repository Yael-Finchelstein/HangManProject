path = input("Please enter file path: ")
func = input("Please choose one of the following functions: [sort, rev or last] ")

with open(path, "r") as file:
    lines = file.readlines()
    if func == 'sort':
        words = set()
        for line in lines:
            for word in line.split(' '):
                words.add(word.replace("\n", ""))
        sorted_words = sorted(list(words))
        print(sorted_words)

    elif func == 'rev':
        for line in lines:
            print(line[::-1])

    elif func == 'last':
        count = 0
        n = int(input("Please enter a number: "))
        last_n_lines = lines[-n:]
        for line in last_n_lines:
            print(line)
