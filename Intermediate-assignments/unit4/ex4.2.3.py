temp_str = input("Please enter temperature: ")
temp = float(temp_str[:-1])
unit = temp_str[-1]

if unit.lower() == 'c':
    f_temp = (9 * temp + 32 * 5) / 5
    print(str(temp) + "°C is " + str(f_temp) + "°F")

elif unit.lower() == 'f':
    c_temp = (5 * temp - 160) / 9
    print(str(temp) + "°F is " + str(c_temp) + "°C")

else:
    print("Invalid temperature suffix. Please use either 'C' or 'F'.")
