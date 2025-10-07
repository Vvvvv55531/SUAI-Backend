import unittest
from scales import Product, Scales


class TestScales(unittest.TestCase):
    def test_add_product(self):
        scales: Scales = Scales(25.0)
        product: Product = Product("orange", "food", 1000.0, 6.0)
        scales.add_product(product)
        self.assertEqual(scales.is_exist(Product("orange", "food", 1000.0, 6.0)), False)
        self.assertEqual(scales.is_empty(), False)

    def test_del_product(self):
        scales: Scales = Scales(25.0)
        product: Product = Product("orange", "food", 1000.0, 6.0)
        scales.add_product(product)
        scales.del_product(product)
        self.assertEqual(scales.is_exist(Product("orange", "food", 1000.0, 6.0)), True)
        self.assertEqual(scales.is_empty(), True)

    def test_is_empty(self):
        scales: Scales = Scales(25.0)
        product: Product = Product("orange", "food", 1000.0, 6.0)
        scales.add_product(product)
        self.assertEqual(scales.is_empty(), False)

    def test_is_exist(self):
        scales: Scales = Scales(25.0)
        self.assertEqual(scales.is_exist(Product("orange", "food", 1000.0, 6.0)), True)
