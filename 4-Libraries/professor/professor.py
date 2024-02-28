import random


def main():
    level = get_level()
    score = counting_round(level)
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


def counting_wrong(x, y, current_question, tries):
    while tries < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                tries += 1
                print("EEE")
        except ValueError:
            tries = 3
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False


def counting_round(level):
    round = 1
    score = 0
    current_question = None
    tries = 0
    while round <= 10:
        x, y = generate_integer(level)
        current_question = (x, y)
        response = counting_wrong(x, y, current_question, tries)
        if response == True:
            score += 1
            round += 1
            tries = 0
        elif tries == 3:
            round += 1
            tries = 0
    return score


if __name__ == "__main__":
    main()
