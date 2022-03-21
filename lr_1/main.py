from parse_text import Parser
import input_handler as inp
import re


def main():
    user_choice = inp.file_input()
    k, n = inp.def_nk()

    pars = Parser(n, k, user_choice)
    pars.print_information()


if __name__ == "__main__":
    main()
