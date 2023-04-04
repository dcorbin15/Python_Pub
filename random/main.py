# Darius Corbin
# 11/18/022
# Basic Calendar


import calendar

# Ask the user for a year and month
year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))

# Use the calendar module to generate the calendar
cal = calendar.monthcalendar(year, month)

# Define the labels for the days of the week
days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

# Print the calendar
print("{0:^20}".format(calendar.month_name[month]))
print("{0:^20}".format(year))
for day in days:
    print("{0:<3}".format(day), end='')
print()
for week in cal:
    for day in week:
        if day == 0:
            print("{0:<3}".format(""), end='')
        else:
            print("{0:<3}".format(day), end='')
    print()
