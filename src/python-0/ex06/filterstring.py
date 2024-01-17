import sys
from ft_filter import ft_filter


def main():
    """
    This function filters and prints a list of words
    according to a given length.
    Arguments:
        - words: a list of words
        - length: the length to filter
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        condition = all(char.isalnum() or char.isspace() for char in sys.argv[1])
        assert condition, "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
        
        value = sys.argv[1].split(' ')
        print(ft_filter(lambda x: len(x) > int(sys.argv[2]), value))
    except AssertionError as error:
        print(f"{AssertionError.__name__} : {error}")


if __name__ == "__main__":
    main()