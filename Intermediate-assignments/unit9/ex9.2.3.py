def who_is_missing(file_name):
    with open(file_name) as file:
        numbers = file.read().split(",")

    numbers = [int(num) for num in numbers]
    numbers.sort()

    for i in range(1, len(numbers) + 1):
        if numbers[i-1] != i:
            missing_number = i
            break

    with open("found.txt", "w") as file:
        file.write(str(missing_number))
    return missing_number
