from unittest import TestCase

from TennisJudge import TennisJudge


class TestTennisJudge(TestCase):
    def test_love_all(self):
        self.assertEqual("Love All", TennisJudge.judge("Eric", "James", 0, 0))

    def test_love_fifteen(self):
        self.assertEqual("Love Fifteen", TennisJudge.judge("Eric", "James", 0, 1))

    def test_love_thirty(self):
        self.assertEqual("Love Thirty", TennisJudge.judge("Eric", "James", 0, 2))

    def test_love_forty(self):
        self.assertEqual("Love Forty", TennisJudge.judge("Eric", "James", 0, 3))

    def test_fifteen_love(self):
        self.assertEqual("Fifteen Love", TennisJudge.judge("Eric", "James", 1, 0))

    def test_thirty_love(self):
        self.assertEqual("Thirty Love", TennisJudge.judge("Eric", "James", 2, 0))

    def test_fifteen_all(self):
        self.assertEqual("Fifteen All", TennisJudge.judge("Eric", "James", 1, 1))

    def test_thirty_all(self):
        self.assertEqual("Thirty All", TennisJudge.judge("Eric", "James", 2, 2))

    def test_deuce(self):
        self.assertEqual("Deuce", TennisJudge.judge("Eric", "James", 3, 3))

    def test_eric_adv(self):
        self.assertEqual("Eric Adv", TennisJudge.judge("Eric", "James", 4, 3))

    def test_james_adv(self):
        self.assertEqual("James Adv", TennisJudge.judge("Eric", "James", 3, 4))

    def test_james_win(self):
        self.assertEqual("James Win", TennisJudge.judge("Eric", "James", 3, 5))

    def test_eric_win(self):
        self.assertEqual("Eric Win", TennisJudge.judge("Eric", "James", 6, 4))

