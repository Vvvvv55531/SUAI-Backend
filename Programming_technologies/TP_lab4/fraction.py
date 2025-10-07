
class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")
        self._num: int = numerator
        self._den: int = denominator

    def __str__(self) -> str:
        return f"{self._num}/{self._den}"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        new_num = self._num * other._den - other._num * self._den
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        new_num = self._num * other._num
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        new_num = self._num * other._den
        new_den = self._den * other._num
        return Fraction(new_num, new_den)
