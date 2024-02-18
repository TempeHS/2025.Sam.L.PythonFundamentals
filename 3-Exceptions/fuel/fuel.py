def main():
    percent = fuel_calculate()
    print(f"The fuel percentage is {percent}%")
    if percent <= 1:
        print("E")
    elif 1 < percent <= 100:
        print("F")


def fuel_calculate():
    while True:
        try:
            X, Y = map(int, input("The fraction is: ").split("/"))
            if X > 4:
                raise UnboundLocalError
            fuel_percent = (X / Y) * 100
        except ValueError:
            print("Please enter an Interger!")
        except ZeroDivisionError:
            print("Cannot perform a division operator with zero as a second argument")
        except UnboundLocalError:
            print("Only accept first argument (X) less than or equal to 4")
        else:
            break
    return fuel_percent


main()
