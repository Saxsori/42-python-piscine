import sys


def main():
    morse_code = {
        'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
        'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',
        'O': '---',    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',
        'T': '-',      'U': '..-',    'V': '...-',   'W': '.--',
        'X': '-..-',   'Y': '-.--',   'Z': '--..',   ' ':  "/ ",
        '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
        '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
        '8': '---..',  '9': '----.'
    }

    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        condition = all(char.isalnum() or char.isspace() for char in sys.argv[1])
        assert condition, "the arguments are bad"
        print("".join((morse_code[item] + " ") for item in sys.argv[1].upper()))
    except AssertionError as error:
        print(f"{AssertionError.__name__} : {error}")
	

if __name__ == "__main__":
    main()
