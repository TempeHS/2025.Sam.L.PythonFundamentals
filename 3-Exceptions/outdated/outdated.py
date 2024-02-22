months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}

date = ""
while True:
    str = input("Valid date: ")
    # Check if the date is in the format "Month Day, Year"
    if str[0:2].isalpha():
        iso_date = str.replace(",", "")
        try:
            month, day, year = iso_date.split(" ")
        except ValueError:
            print("Enter a valid date:")
            continue
    # Check if the date is in the format "Day/Month/Year"
    elif str.count("/") == 2:
        try:
            day, month, year = str.split("/")
        except ValueError:
            print("Enter a valid date:")
            continue
    else:
        print("Enter a valid date:")
        continue
    # Day check: 0 < day < 32
    if int(day) > 0 and int(day) < 32:
        date += year
        date += "-"
    else:
        date = ""
        print("Enter a valid date:")
        continue
    # Month check:
    #   Non-Numeric: Check dict, if not, fails
    #   Numeric: Check 0 < month < 13
    if not month.isnumeric():
        if month in months:
            date += months[month]
            date += "-"
        else:
            date = ""
            print("Enter a valid date:")
            continue
    elif int(month) < 13 and int(month) > 0:
        date += "{:02d}-".format(int(month))
    else:
        date = ""
        print("Enter a valid date:")
        continue
    # Day check: 0 < day < 32
    if int(day) > 0 and int(day) < 32:
        date += "{:02d}".format(int(day))
        break
    else:
        date = ""
        print("Enter a valid date:")
        continue
print(date)
