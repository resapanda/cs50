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

# input 8/6/1999 or August 6, 1999
# output 1999-8-6
dateList = []
new = ""

while True:
    date = input("Date: ")
    if "/" in date:
        dateList = date.split("/")
        if 0 < int(dateList[0]) <= 12 and 0 < int(dateList[1]) <= 31 and len(dateList[2]) == 4:
            print(dateList[2] + "-" + dateList[0].zfill(2) + "-" + dateList[1].zfill(2))
            break
        else:
            continue
    elif "," in date:
        new = date.replace(",", "")
        dateList = new.split()
        if 0 < int(dateList[1]) <= 31 and len(dateList[2]) == 4 and dateList[0] in months:
            print(dateList[2] + "-" + str(months[dateList[0]]).zfill(2) + "-" + dateList[1].zfill(2))
            break
        else:
            continue
    else:
        continue





