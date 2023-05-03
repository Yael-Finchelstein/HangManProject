import calendar

date_str = input("Please enter a date [dd/mm/yyyy format]: ")
day = int(date_str[:2])
month = int(date_str[3:5])
year = int(date_str[6:])

weekday_num = calendar.weekday(year, month, day)
weekday_name = calendar.day_name[weekday_num]

print(weekday_name)
