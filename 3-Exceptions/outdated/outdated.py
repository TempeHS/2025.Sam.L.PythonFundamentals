str = input("Valid date: ")
months = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12",
}

date = ""
while True:
    if str[0:2].isnumeric():
        iso_date = str.replace(",", "")
        try:
            months, day, year = iso_date.split(" ")
        except ValueError:
            print("Enter a valid date:")
    else:
        try:
            month, day, year = str.split("/")
        except ValueError:
            str = input("Enter a valid date: ")
            continue
    # Day check: 0 < day < 32
    if int(day) > 0 and int(day) < 32:
        date += day
        date += "-"
    else:
        date = ""
        str = input("Enter a valid date: ")
        continue
    # Month check:
    #   Non-Numeric: Check dict, if not, fails
    #   Numeric: Check 0 < month < 13
    if not month.isnumeric():
        if month in dict:
            date += dict[month]
            date += "-"
        else:
            date = ""
            str = input("Enter a valid date: ")
            continue
    elif int(month) < 13 and int(month) > 0:
        date += month
        date += "-"
    else:
        date = ""
        str = input("Enter a valid date: ")
        continue
    # Year check: year > 0
    if int(year) > 0:
        date += year
        break
    else:
        str = input("Enter a valid date: ")
        continue
print(date)
