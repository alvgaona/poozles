import unittest

from buy_sell_stock import buy_sell_stock


class TestBuyAndSellStock(unittest.TestCase):
    def test_buy_and_sell(self):
        self.assertEqual(buy_sell_stock([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(buy_sell_stock([1, 2]), 1)
        self.assertEqual(buy_sell_stock([7, 5, 4, 3, 1]), 0)
