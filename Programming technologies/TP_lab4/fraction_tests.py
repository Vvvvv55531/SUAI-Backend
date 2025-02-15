import unittest
from fraction import Fraction


class TestFridge(unittest.TestCase):
    def test_add(self):
        f1 = Fraction(2, 5)
        f2 = Fraction(1, 3)
        res = f1 + f2
        self.assertEqual(res.__str__(), "11/15")

    def test_sub(self):
        f1 = Fraction(2, 5)
        f2 = Fraction(1, 3)
        res = f1 - f2
        self.assertEqual(res.__str__(), "1/15")

    def test_mul(self):
        f1 = Fraction(2, 5)
        f2 = Fraction(1, 3)
        res = f1 * f2
        self.assertEqual(res.__str__(), "2/15")

    def test_div(self):
        f1 = Fraction(2, 5)
        f2 = Fraction(1, 3)
        res = f1 / f2
        self.assertEqual(res.__str__(), "6/5")
