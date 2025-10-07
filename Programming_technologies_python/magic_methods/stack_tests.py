import unittest
from stack import Stack


class TestFridge(unittest.TestCase):
    def test_str(self):
        stack: Stack = Stack[int](1)
        stack(1)
        self.assertEqual(stack.__str__(), "Stack: [1]")

    def test_len(self):
        stack: Stack = Stack[int](1)
        stack(2)
        self.assertEqual(len(stack), 1)

    def test_call(self):
        stack: Stack = Stack[int](0)
        with self.assertRaises(ValueError):
            stack(1)

    def test_delitem(self):
        stack: Stack = Stack[int](0)
        with self.assertRaises(ValueError):
            del stack[1]
        with self.assertRaises(ValueError):
            del stack[-1]
