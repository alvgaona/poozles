import unittest

from running_sum import running_sum


class TestRunningSum(unittest.TestCase):
    def test_running_sum(self):
        self.assertEqual(running_sum([1, 2, 3, 4, 5]), [1, 3, 6, 10, 15])
