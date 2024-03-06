def main():
    fraction = input("Fraction: ")
    fraction_convert = convert(fraction)
    output = gauge(fraction_convert)
    print(output)


def convert(fraction):
    while True:
        try:
            num, denum = fraction.split("/")
            new_num = int(num)
            new_denum = int(denum)
            r = new_num / new_denum
            if r <= 1:
                P = int(r * 100)
                return P
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        # Change from str to int to fail the test
        return int(percentage) + "%"


if __name__ == "__main__":
    main()
