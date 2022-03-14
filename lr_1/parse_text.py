import re


class Parser:
    def __init__(self, n: int, k: int, file: str) -> None:
        self._n = n
        self._k = k
        self._file = file

    def print_information(self):
        lines = self.init_text()

        sentences = self.split_lines(lines)
        words = self.split_sentences(sentences)

        words_count = self.words_repetition(words)
        pass

    def words_repetition(self, words):
        counter = {}
        for word in words:
            count = counter.get(word, 0)
            counter.update({word: count + 1})

        for word in counter:
            print(word, ":", counter[word])
        return counter


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

        words = list(filter(lambda word: word != '', words))

        return words
