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
