import unittest

from dinousaurs import gather_dinosaurs, create_sorted_dinosaurs


class TestDinoaurs(unittest.TestCase):
    def test_dinosaurs(self):
        with open('dataset1.csv') as f1, open('dataset2.csv') as f2:
            lines1 = f1.readlines()[1:]
            lines2 = f2.readlines()[1:]
        
            dino_dict = gather_dinosaurs(lines1, lines2)
            dinosaurs = create_sorted_dinosaurs(dino_dict)
            self.assertEqual(len([dino for dino in dinosaurs if dino.stance == 'bipedal']), 5)
