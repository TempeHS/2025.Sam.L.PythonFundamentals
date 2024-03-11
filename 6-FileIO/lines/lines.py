import sys


def main():

    check_command_line_arg()

    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File is not found")
    count_line = 0
    for line in lines:
        if check_comment_or_empty_line(line) == False:
            count_line += 1
    print(count_line)


def check_command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments ")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")


def check_comment_or_empty_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False


if __name__ == "__main__":
    main()
