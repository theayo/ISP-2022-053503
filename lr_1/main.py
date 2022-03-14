from parse_text import Parser
import re


def main():
    # name = input("FIle name:")
    # name = "Empty"
    # name = "Text"
    name = "Some_words"
    # name = "one_two_three"

    ma = Parser(4, 10, name)
    ma.print_information()
    pass


if __name__ == "__main__":
    main()
