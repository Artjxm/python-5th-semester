# программа для тестирования модулей

import unittest

from guesser import Guesser

class TestGuesser(unittest.TestCase):

    def setUp(self):
        self.guesser = Guesser("word")

    def test_1(self):
        self.assertEqual(self.guesser.is_geussed(), False)
        pass

    if __name__ == "__main__":
        unittest.main()
