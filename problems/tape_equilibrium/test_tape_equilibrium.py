import unittest


from tape_equilibrium import tape_equilibrium


class TestTapeEquilibrium(unittest.TestCase):
    def test_tape_equilibrium(self):
        A = [-10, -20, -30, -40, 100]
    
        self.assertEqual(tape_equilibrium(A), 20)
