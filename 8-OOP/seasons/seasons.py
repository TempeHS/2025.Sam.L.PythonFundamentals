from datetime import date
from datetime import timedelta
import sys


def main():
    try:
        date_ob = get_dates()
        date_ob = date(date_ob[0], date_ob[1], date_ob[2])
        print(date_ob)
    except ValueError:
        print("Invalid date")
        sys.exit(1)


# def get_date():
# year = int(input("Enter year:"))
# month = int(input("Enter month:"))
# day = int(input("Enter day:"))
# return year, month, day


def get_dates():
    try:
        year, month, day = sys.argv[1:]
        return int(year), int(month), int(day)
    except ValueError:
        sys.exit(1)


def convert_min():
    # 1 year = 365 x 24 x 60 = 525,600
    # leap year = 1 x 24 x 60 = 1440 extra minutes
    year = timedelta(minutes=525600)
    year


if __name__ == "__main__":
    main()
