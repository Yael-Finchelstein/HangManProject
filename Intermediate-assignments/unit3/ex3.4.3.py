string = input("Please enter a string: ")
length = len(string)
half_index = length // 2

first_half = string[:half_index]
second_half = string[half_index:]

print_string = first_half.lower() + second_half.upper()

print(print_string)
