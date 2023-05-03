char = input("Please enter your guess: ")

if len(char) == 1:
    if char.isalpha():
        print(char.lower())
    else:
        print("E2")

elif len(char) > 1:
    if char.isalpha():
        print("E1")
    elif char.isascii():
        print("E3")
