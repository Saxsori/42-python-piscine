import sys


def main():
    """
    This function counts the number of characters in a text.
    The text can be provided as an argument or as an input.
    It counts the number of upper and lower letters,
    punctuation marks, spaces and digits.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if (len(sys.argv) == 1):
            value = input("What is the text to count?\n")
        else:
            value = sys.argv[1]
        print("The text contains {} characters:".format(len(value)))
        print("{} upper letters".format(sum(1 for c in value if c.isupper())))
        print("{} lower letters".format(sum(1 for c in value if c.islower())))

        punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        punctuation_marks_num = sum(1 for c in value if c in punctuation_marks)

        print("{} punctuation marks".format(punctuation_marks_num))
        print("{} spaces".format(sum(1 for c in value if c.isspace())))
        print("{} digits".format(sum(1 for c in value if c.isdigit())))

    except AssertionError as error:
        print(f"{AssertionError.__name__} : {error}")
    except EOFError:
        print(f"{EOFError.__name__} : provided text is empty")


if __name__ == "__main__":
    main()
