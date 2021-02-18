import unittest


from remove_duplicates import remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    
        self.assertEqual(remove_duplicates(nums), 5)
