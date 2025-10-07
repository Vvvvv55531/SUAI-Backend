import unittest
from fridge_and_freezer import Products, Fridge


class TestFridge(unittest.TestCase):
    def test_add_product(self):
        fridge: Fridge = Fridge(3.0)
        product: Products = Products("apple", 20.3, -20.3)
        fridge.add_product(product)
        self.assertEqual(fridge.is_exist(Products("apple", 20.3, -20.3)), False)
        self.assertEqual(fridge.is_empty(), False)

    def test_del_product(self):
        fridge: Fridge = Fridge(3.0)
        product: Products = Products("apple", 20.3, -20.3)
        fridge.add_product(product)
        fridge.del_product(product)
        self.assertEqual(fridge.is_exist(Products("apple", 20.3, -20.3)), True)
        self.assertEqual(fridge.is_empty(), True)

    def test_is_empty(self):
        fridge: Fridge = Fridge(3.0)
        product: Products = Products("apple", 20.3, -20.3)
        fridge.add_product(product)
        self.assertEqual(fridge.is_empty(), False)

    def test_is_exist(self):
        fridge: Fridge = Fridge(3.0)
        self.assertEqual(fridge.is_exist(Products("apple", 20.3, -20.3)), True)
