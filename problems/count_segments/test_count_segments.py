import unittest

from count_segments import count_segments


class TestCountSegments(unittest.TestCase):
    def test_count_segments(self):
        self.assertEqual(count_segments('Hello, my name is John'), 5)