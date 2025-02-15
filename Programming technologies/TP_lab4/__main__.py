from stack import Stack
from fraction import Fraction

if __name__ == '__main__':

    print("------Stack------")
    stack: Stack = Stack[int](5)

    stack(5)
    stack(3)
    stack(1)
    stack(4)
    stack(2)
    print(stack)
    print("Size:", len(stack), "\n")

    del stack[-1]
    del stack[-1]
    print(stack)
    print("Size:", len(stack))

    print("\n------Fraction------")
    f1 = Fraction(2, 5)
    f2 = Fraction(1, 3)

    res = f1 + f2
    print(f"{f1} + {f2} = {res}")
    res = f1 - f2
    print(f"{f1} - {f2} = {res}")
    res = f1 * f2
    print(f"{f1} * {f2} = {res}")
    res = f1 / f2
    print(f"{f1} / {f2} = {res}")
