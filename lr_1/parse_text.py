import re
from statistics import median, mean


class Parser:
    def __init__(self, n: int, k: int, file: str) -> None:
        self._n = n
        self._k = k
        self._file = file

    def print_information(self):
        lines = self.init_text()
        if lines is None:
            return

        sentences = self.split_lines(lines)
        words = self.split_sentences(sentences)

        print()
        self.print_words_repetitions(words)
        counter_words = self.get_words_count(sentences)
        print(f"\nAverage word count: {self.get_avg_words(counter_words)}")
        print(f"Median value: {self.get_median_word(counter_words)}")
        self.print_n_grams(words)
        print()

    def print_words_repetitions(self, words):
        counter = self.get_words_repetition(words)
        for word in counter:
            print(word, ":", counter[word], end=" ")

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
        return int(mean(counter_words))

    def get_median_word(self, count_word):
        return int(median(count_word))

    def print_n_grams(self, words):
        big_word = ""
        for word in words:
            big_word += word

        size = self._n
        healling_slave = dict()
        for i in range(len(big_word) - size + 1):
            temp = big_word[0 + i:i + size]
            if temp in healling_slave:
                healling_slave[temp] += 1
            else:
                healling_slave[temp] = 1
        d = {k: healling_slave[k] for k in sorted(healling_slave, key=healling_slave.get, reverse=True)}

        i = 1
        for key, value in d.items():
            if i > self._k:
                break
            print(f"{key}: {value}", end=" ")
            i += 1

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
