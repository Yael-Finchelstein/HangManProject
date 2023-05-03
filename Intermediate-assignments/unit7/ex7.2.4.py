def seven_boom(end_number):
    list = []
    for number in range(0, end_number + 1):
        if number % 7 == 0 or "7" in str(number):
            list.append('BOOM')
        else:
            list.append(number)
    return list
