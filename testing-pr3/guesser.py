# программа с ядром игры

class Guesser:
    def __init__(self, word):
        self.word = word
        self.opened = ['?' for _ in range(len(word))]

    def is_geussed(self):
        for ch in self.opened:
            if ch == '?':
                return False
        return True