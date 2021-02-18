import unittest

from top_k_words import top_k_sorting, top_k_heap


class TestTopKWords(unittest.TestCase):
    def test_top_k_sorting(self):
        self.assertEqual(top_k_sorting(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2), ['i', 'love'])
        self.assertEqual(top_k_sorting(['aaa', 'aa', 'a'], 1), ['a'])

    def test_top_k_heap(self):
        self.assertEqual(top_k_heap(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2), ['i', 'love'])
        self.assertEqual(top_k_heap(['aaa', 'aa', 'a'], 1), ['a'])
