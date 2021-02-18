import unittest


from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        items = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1])
        ]
    
        for item in items:
            numbers, target, expected = item
            self.assertEqual(two_sum(numbers, target), expected)
