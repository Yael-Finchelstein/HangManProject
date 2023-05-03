string = input("Please enter a string: ")
first_char = string[0]
new_string = first_char + string[1:].replace(first_char, 'e')

print(new_string)
