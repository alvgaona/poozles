import unittest

from camelcase import camelcase


class TestCamelCase(unittest.TestCase):
    def test_camelcase(self):
        text = "saveChangesInTheEditor"

        self.assertEqual(camelcase(text), 5)
