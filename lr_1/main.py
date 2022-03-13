from parse_text import Parser
import re


def main():
    # name = input("FIle name:")
    # name = "Empty"
    name = "Text"

    ma = Parser(1, 2, name)
    ma.print_information()
    pass


if __name__ == "__main__":
    main()
