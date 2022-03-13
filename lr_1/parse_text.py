import re


class Parser:
    def __init__(self, n: int, k: int, file: str) -> None:
        self._n = n
        self._k = k
        self._file = file

    def print_information(self):
        lines = self.init_text()
        print(lines)
        sentences = self.split_lines(lines)
        print(sentences)
        words = self.split_sentences(sentences)
        print(words)
        pass

    def count_words(self):
        pass

    def median_word(self):
        pass

    def n_grams(self):
        pass

    def information(self):
        pass

    def init_text(self):
        lines = []

        with open("data/" + self._file + ".txt", 'r') as file:
            file.seek(0)
            lines = file.readlines()
        file.close()
        if not lines:
            print("empty!")
            return
        return lines

    def split_lines(self, lines):
        sentence = []
        for line in lines:
            sentence += re.split(r"\. |! |; |:", line)
        return sentence

    def split_sentences(self, sentences):
        words = []
        for sentence in sentences:
            words += re.split(r"[ ,\n]", sentence)

        for word in words:
            word.lower()

        return words