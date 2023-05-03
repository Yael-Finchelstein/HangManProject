dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}

choice = int(input("Enter a number between 1 and 7: "))

if choice == 1:
    print(dict["last_name"])
elif choice == 2:
    print(dict["birth_date"].split(".")[1])
elif choice == 3:
    print(len(dict["hobbies"]))
elif choice == 4:
    print(dict["hobbies"][-1])
elif choice == 5:
    dict["hobbies"].append("Cooking")
elif choice == 6:
    (day, month, year) = dict["birth_date"].split(".")
    print((day, month, year))
elif choice == 7:
    birth_year = dict["birth_date"].split(".")[-1]
    age = 2023 - int(birth_year)
    dict["age"] = age
    print(dict["age"])
