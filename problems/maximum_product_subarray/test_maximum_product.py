import unittest

from maximum_product import maximum_product_bf, maximum_product_opt


class TestMaximumProduct(unittest.TestCase):
    def test_maximum_product(self):
        nums = [1, 2, 3, 4]
        
        self.assertEqual(maximum_product_bf(nums), (24, 0, 3))
        self.assertEqual(maximum_product_opt(nums), (24, 0, 3))
