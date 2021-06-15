import re
import sys


def count_words(filename):
    """
    Opening the file, trimming special chars and counting frequency of words.

    :param filename: Name of the file.
    :return: List of tuples, key is word and value is count.
    """
    with open(filename, encoding='utf8') as f:
        text = re.sub(r'[^\w\s]', '', f.read()).lower().split()

    counter_list = [(w, text.count(w)) for w in list(set(text))]

    return counter_list


def print_words(filename):
    """
    Prints words from the file and how many times they appear.

    :param filename: Name of the file.
    """
    counter_list = count_words(filename)
    counter_list.sort()

    print('\n'.join([f'{a} {b}' for a, b in counter_list]))


def print_top(filename):
    """
    Prints top 20 words from the file and how many times they appear.

    :param filename: Name of the file.
    """
    counter_list = count_words(filename)
    counter_list.sort(key=lambda t: t[1], reverse=True)

    print('\n'.join([f'{t[0]} {t[1]}' for i, t in enumerate(counter_list) if i < 20]))


def main():
    """
    Main program.
    """
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
