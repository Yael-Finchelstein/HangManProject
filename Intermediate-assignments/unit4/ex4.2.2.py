string = input("Please enter a string: ")
string = string.replace(" ", "").lower()

if string == string[::-1]:
    print("OK")
else:
    print("NOT")
