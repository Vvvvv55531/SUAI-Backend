from Numbers import check
from Students import read_students_file, max_students_group, max_straight_a_group
from Table import Table, Item
from Wallet import Wallet
import unittest


class TestScales(unittest.TestCase):
    def test_check(self):
        num = 0
        self.assertEqual(check(num), 3)

    def test_max_students_group(self):
        students_data = read_students_file("Students.txt")
        self.assertEqual(max_students_group(students_data), "4217")

    def test_max_straight_group(self):
        students_data = read_students_file("Students.txt")
        self.assertEqual(max_straight_a_group(students_data), "4217")

    def test_add_item(self):
        item = Item("Fork", 5)
        table = Table(5)
        self.assertEqual(table.add_item(item), True)

    def test_remove_item(self):
        item = "Fork"
        table = Table(5)
        self.assertEqual(table.remove_item(item), False)

    def test_add_money(self):
        wallet = Wallet()
        self.assertEqual(wallet.add_money("RUB", 10000.0), False)

    def test_total_in_currency(self):
        wallet = Wallet()
        wallet.add_money("RUB", 10000.0)
        self.assertEqual(wallet.total_in_currency("RUB", 11.0), 10000.0)

    def test_amount_in_currency(self):
        wallet = Wallet()
        wallet.add_money("RUB", 10000.0)
        self.assertEqual(wallet.amount_in_currency("RUB"), 10000.0)
