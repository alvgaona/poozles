#!/bin/python3
from math import sqrt


class Dinosaur(object):
    __g = 9.8

    def __init__(self, name: str, leg_length: float, stride_length: float, stance: str, diet: str) -> None:
        self.name = name
        self.leg_length = leg_length
        self.stride_length = stride_length
        self.stance = stance
        self.diet = diet

    def __str__(self):
        return "Name: {}, Speed: {}, Stance: {}, Diet: {}, Leg Length: {}, Stride Length: {}" \
            .format(self.name, self.speed(), self.stance, self.diet, self.leg_length, self.stride_length)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.speed() < other.speed()

    def __gt__(self, other):
        return self.speed() > other.speed()

    def speed(self):
        if self.leg_length is None or self.stride_length is None:
            return 0

        return ((self.stride_length / self.leg_length) - 1) * sqrt(self.leg_length * Dinosaur.__g)


def gather_dinosaurs(lines1, lines2):
    dino_dict = {}

    for line in lines1:
        line = line.replace('\n', '').split(',')
        dinosaur = line[0]
        dino_dict[dinosaur] = {}
        dino_dict[dinosaur]['stride_length'] = line[1]
        dino_dict[dinosaur]['stance'] = line[2]

    for line in lines2:
        line = line.replace('\n', '').split(',')
        dinosaur = line[0]

        if dino_dict.get(dinosaur) is None:
            dino_dict[dinosaur] = {}

        dino_dict[dinosaur]['leg_length'] = line[1]
        dino_dict[dinosaur]['diet'] = line[2]

    return dino_dict


def create_sorted_dinosaurs(dino_dict: dict) -> list:
    dinosaurs = []
    for k, v in dino_dict.items():
        leg_length = v.get('leg_length')
        stride_length = v.get('stride_length')

        if leg_length is not None:
            leg_length = float(leg_length)

        if stride_length is not None:
            stride_length = float(stride_length)

        dinosaurs.append(Dinosaur(k, leg_length, stride_length, v.get('stance'), v.get('diet')))

    return sorted(dinosaurs, key=lambda x: x.speed(), reverse=True)


def main(*args, **kwargs):
    file1 = 'dataset1.csv'
    file2 = 'dataset2.csv'

    with open(file1) as f1, open(file2) as f2:
        lines1 = f1.readlines()[1:]
        lines2 = f2.readlines()[1:]

        dino_dict = gather_dinosaurs(lines1, lines2)

        dinosaurs = create_sorted_dinosaurs(dino_dict)

        [print(dino) for dino in dinosaurs if dino.stance == 'bipedal']


if __name__ == '__main__':
    exit(main())
