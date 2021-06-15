import sys


def last(string):
    return string[len(string) - 1]


try:
    print(*sorted(sys.argv[1:], key=last), sep="\n")
except Exception:
    print("Invalid input")
