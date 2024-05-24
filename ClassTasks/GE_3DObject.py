import math


class Square:
    def __init__(self, length, width, height):
        if not int:
            raise ValueError("Length, width, and height must be integers")
        self.length = length
        self.width = width
        self.height = height
        self.volume = length * width * height
        self.area = length * width

    @classmethod
    def square_dimen(cls):
        length = int(input("Length of square is: "))
        width = int(input("Width of square is: "))
        height = int(input("Height of square is: "))
        return cls(length, width, height)

    def from_area(cls):
        return cls.area

    def from_volume(cls):
        return cls.volume


class TrianglePy:
    def __init__(self, height, length):
        if not int:
            raise ValueError("Length, width, and height must be integers")
        self.height = height
        self.length = length

    @classmethod
    def square_dimen(cls, length, width, height):
        length = int(input("Length of square is: "))
        width = int(input("Width of square is: "))
        height = int(input("Height of square is: "))
        return cls(length, width, height)

    def from_area(cls):
        return cls.area

    def from_volume(cls):
        return cls.volume


class Sphere:
    def __init__(self, radius):
        if not int:
            raise ValueError("Radius must be an integer")
        self.radius = radius

    @staticmethod
    def pi_num(pi):
        return pi == 3.14

    @classmethod
    def from_sAreaNvolume(cls, pi, radius):
        return cls(area=4 * pi * radius * 2, volume=4 / 3 * pi * radius * 3)
