"""In a file called outdated.py,
implement a program that prompts the user for a date, anno Domini,
in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below:
"""

"""Then output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days;
no need to validate whether a month has 28, 29, 30, or 31 days."""

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

days = {
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31
}

# input 8/6/1999 or August 6, 1999
# output 1999-8-6

date = []

while True:
    try:
        date = input("Date: ").split("/" and "," and " ")
        if date[1] in months and date[2] in days and len(date[3]) == 4:
            break
    except KeyError:
        continue

print(date[3], "-", date[1], "-", date[2])





