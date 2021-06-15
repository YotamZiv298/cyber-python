import argparse

FILE_NAME = __file__.split('/')[-1]

OPERATION = 'operation'
OPERATION_HELP = 'math function'
OPERATION_TYPE = str

PARAM1 = 'first_number'
PARAM1_HELP = 'first number'
PARAM1_TYPE = int

PARAM2 = 'second_number'
PARAM2_HELP = 'second number'
PARAM2_TYPE = int


def add(a, b):
    """
    Prints addition between two parameters.

    :param a: Number.
    :param b: Number.
    """
    print(a + b)


def multiply(a, b):
    """
    Prints multiplication between two parameters.

    :param a: Number.
    :param b: Number.
    """
    print(a * b)


def subtract(a, b):
    """
    Prints subtraction between two parameters.

    :param a: Number.
    :param b: Number.
    """
    print(a - b)


def divide(a, b):
    """
    Prints division between two parameters.

    :param a: Number.
    :param b: Number.
    """
    print(a / b)


def check_operation():
    """
    Checks operation based on script parameters and activate functions accordingly.
    """
    if args['w']:
        print("Good morning :)")
    if args[OPERATION] == add.__name__:
        add(args[PARAM1], args[PARAM2])
    elif args[OPERATION] == subtract.__name__:
        subtract(args[PARAM1], args[PARAM2])
    elif args[OPERATION] == multiply.__name__:
        multiply(args[PARAM1], args[PARAM2])
    elif args[OPERATION] == divide.__name__:
        divide(args[PARAM1], args[PARAM2])


# Creating parser
parser = argparse.ArgumentParser(FILE_NAME)

# Adding arguments
parser.add_argument(OPERATION, choices=[add.__name__, subtract.__name__, multiply.__name__, divide.__name__],
                    help=OPERATION_HELP, type=OPERATION_TYPE)
parser.add_argument(PARAM1, help=PARAM1_HELP, type=PARAM1_TYPE)
parser.add_argument(PARAM2, help=PARAM2_HELP, type=PARAM2_TYPE)
parser.add_argument('-w', action='store_true')
args = vars(parser.parse_args())

check_operation()
