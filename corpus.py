__author__ = 'bengt'


class Corpus(object):
    def __init__(self, filename):
        self.sentences = []

        with open(filename) as f:
            lines = f.readlines()
            self.sentences = self.parse_sentences(lines)

    @staticmethod
    def parse_sentences(lines):
        sentences = []
        sentence = [[0, '<s>', '<s>', '<s>', '<s>', '<s>']]
        for line in lines:
            if line == '\n':
                # new sentence
                sentences.append(sentence)
                sentence = [[0, '<s>', '<s>', '<s>', '<s>', '<s>']]
                continue

            sentence.append(line.replace('\n', '').split('\t'))
        return sentences

    def get_sentences(self):
        return self.sentences