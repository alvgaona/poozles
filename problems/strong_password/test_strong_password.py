import unittest

from strong_password import strong_password


class TestStrongPassword(unittest.TestCase):
    def test_strong_password(self):
        password = 'Ab1'
        self.assertEqual(strong_password(len(password), password), 3)
