INPUT_TXT = "YXu0hYq1xQ4,hQXUCw8Cs7nIu8BAxIUADYf\n\nLRYUYw5LI0RYUUYs6hDXU3UIoIBbcm\n.CBSA5LI7RYUUYs2hDXU8YBbnIj\n" \
            ".UIoIBbnI2LI8RYUUYs7hDXU2cYBbnQZ\n.cYBbnQo1LI9RYUUYs7hDXU4UDBk\n.JYUDoIBbnQo4LI3RYUUYs8hDXU6YLRDbj\n" \
            ".JYULYh8LI3RYUUYs8hDXU1CUIBIsDJDYH\n.YLhYJ7BDIoYbj\n.LUhAQo0LYLDo3U" \
            "'hYRD2BDIoYbL2XSAQhY0QU0MDYRs0YXU4XSAQXUBW\n.LYBAR8CUIBDoIUoDRb1LUDYs2LRQRRm\n" \
            ".CUIRAb3JBAQXL6RYlYh9LLDb0LLYBha\n.CBUhYBIL0CBUIoIBbcY9hg\n.JYohYBIL1YXU5YoDx7xQ6," \
            "CUIASIsnD8YLAxYR0YXU9hQIUDUbnYU4QU3YRYXu\n.LLYAS1JBAQXL7Ys3--YhQ2JhD2CBsDRYxYRb2CBhQ9YhQ6LAQIlsQ" \
            "--9CDO7QU1QJ0XSAQXUBW\n.UI4UDXU5CDO0CDn2UQh7Ys2LAQIlsQ0UD2ULRIx8LLYBhA2YR'AQC1OQe\n" \
            ".XoUAv7LI3RYUUYs0hDXU8XSAQXUBW\n.RYlYh0RYlYh5LI9hYUxQ0RYUUYs2hDXU8*UXSIR*9xg\n" \
            ".OQh4YXU3hQIUDUhYnYBbnI9LI1JRDX0QU6,hIDBbcY5L'UI3D7JDs6xg\n.DYJI4YXU6hQIUDUhYnYBbnI9LI9CLDY4QU3," \
            "hIDBbcY2UI5CDn4Ys8D8JQQS1LYoDbLYnDe\n.DYJI0YRD9YhQ6ShIMhQX2UDYRS4DYJI3--9L'UYB5QJ8YRQn9xQ0!YLQXU "

ENCODE_DICT = {'s': 'L', 'b': 's', 'w': 'O', 'z': 'G', 'c': 'o', 'J': 'y', 'V': 't', 'P': 'w', 'B': 'f', 'Z': 'q',
               'F': 'k', 'O': 'N', 'u': 'A', 'W': 'r', 'K': 'K', 'a': 'D', 'v': 'l',
               'g': 'S', 'f': 'x', 'x': 'c', 'N': 'e', 'p': 'b', 'U': 'a', 'j': 'P', 'o': 'Q', 'i': 'I', 'M': 'd',
               't': 'U', 'H': 'V', 'X': 'i', 'Y': 'T', 'R': 'H', 'h': 'X', 'L': 'z',
               'G': 'F', 'A': 'W', 'm': 'n', 'T': 'u', 'l': 'B', 'C': 'Z', 'q': 'p', 'D': 'v', 'I': 'g', 'n': 'h',
               'y': 'C', 'S': 'j', 'k': 'M', 'd': 'J', 'Q': 'E', 'e': 'Y', 'r': 'R',
               'E': 'm'}


def reverse_dict(encode_dict):
    """
    Reverses dictionary.

    :param encode_dict: Characters' dictionary.
    :return: Reversed dictionary.
    """
    return {v: k for k, v in encode_dict.items()}


def translate_from_dict(txt, encode_dict):
    """
    Replacing the characters from the encode dictionary with matching characters.

    :param txt: Text.
    :param encode_dict: Characters' dictionary.
    :return: Replaced characters string.
    """
    return ''.join([encode_dict[c] if c in encode_dict else c for c in txt])


def flip_words(txt):
    """
    Flips the word.

    :param txt: Text.
    :return: Flipped word string.
    """
    return ' '.join(txt.split(' ')[::-1])[::-1]


def num_to_space(txt):
    """
    Replaces digits with white spaces.

    :param txt: Text.
    :return: Text with replaced digits.
    """
    return ''.join(' ' if c.isdigit() else c for c in txt)


def snake_restore(txt, encode_dict):
    """
    Snake, solving the hidden message.

    :param txt: Text.
    :param encode_dict: Encode dictionary.
    :return: Solved text.
    """
    txt = num_to_space(txt)
    txt = flip_words(txt)
    txt = translate_from_dict(txt, reverse_dict(encode_dict))

    return txt


def main():
    """
    Main program.
    """
    print(snake_restore(INPUT_TXT, ENCODE_DICT))


if __name__ == '__main__':
    main()
