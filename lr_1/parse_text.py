import re
import statistics as statistics


class Parser:
    def __init__(self, n: int, k: int, file: str) -> None:
        self._n = n
        self._k = k
        self._file = file

    def print_information(self):
        lines = self.init_text()

        sentences = self.split_lines(lines)
        print(sentences)
        words = self.split_sentences(sentences)
        print(words)

        self.print_words_repetitions(words)
        counter_words = self.get_words_count(sentences)
        print(self.get_avg_words(counter_words))
        print(self.get_median_word(counter_words))
        print(self.n_grams(words))

    def print_words_repetitions(self, words):
        counter = self.get_words_repetition(words)
        for word in counter:
            print(word, ":", counter[word])

    def get_words_repetition(self, words):
        counter = {}
        for word in words:
            count = counter.get(word, 0)
            counter[word] = count + 1

        return counter

    def get_words_count(self, sentences):
        counter_words = []
        for sentence in sentences:
            words = self.split_sentences([sentence])

            counter = len(words)
            counter_words.append(counter)

        return counter_words

    def get_avg_words(self, counter_words):
        return statistics.mean(counter_words)

    def get_median_word(self, count_word):
        return statistics.median(count_word)

    def n_grams(self, words):
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

        words = [word.lower() for word in words]

        words = list(filter(lambda one: one != '', words))
        return words
