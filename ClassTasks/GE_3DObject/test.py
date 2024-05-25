from math import pi


class Shape:
    def __init__(self, color, x, y, z):
        self.color = color
        self.x = x
        self.y = y
        self.z = z

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_locX(self):
        self.x = int(input("Set new X: "))

    def set_locY(self):
        self.y = int(input("Set new Y: "))

    def set_locZ(self):
        self.z = int(input("Set new Z: "))


class TriangularPyramid(Shape):
    def __init__(self, color, x, y, z, base_length, height):
        super().__init__(color, x, y, z)
        self.base_length = base_length
        self.height = height

    def get_cross_section_area(self):
        return (self.base_length**2) * (3**0.5) / 4

    def get_cross_section_perimeter(self):
        return 3 * self.base_length

    def get_surface_area(self):
        return (self.base_length**2) * (3**0.5) / 4 + self.base_length * self.height

    def get_volume(self):
        return (self.base_length**2) * self.height / 3

    def get_surface_count(self):
        return 4


class Cube(Shape):
    def __init__(self, color, x, y, z, side_length):
        super().__init__(color, x, y, z)
        self.side_length = side_length

    def get_cross_section_area(self):
        return self.side_length**2

    def get_cross_section_perimeter(self):
        return 4 * self.side_length

    def get_surface_area(self):
        return 6 * self.side_length**2

    def get_volume(self):
        return self.side_length**3

    def get_surface_count(self):
        return 6


class Sphere(Shape):
    def __init__(self, color, x, y, z, radius):
        super().__init__(color, x, y, z)
        self.radius = radius

    def get_cross_section_area(self):
        return pi * self.radius**2

    def get_cross_section_perimeter(self):
        return 2 * pi * self.radius

    def get_surface_area(self):
        return 4 * pi * self.radius**2

    def get_volume(self):
        return 4 / 3 * pi * self.radius**3

    def get_surface_count(self):
        return 1


# Instantiate a sphere (20-diameter circle)
sphere = Sphere("blue", 10, 0, 10, 10)

# Print sphere properties\
print(f"Sphere:")
print(f"Coordinates: {sphere.get_center()}")
print(f"Color: {sphere.color}")
print(f"2D Area: {sphere.get_cross_section_area()}")
print(f"2D Perimeter: {sphere.get_cross_section_perimeter()}")
print(f"3D Volume: {sphere.get_volume()}")
print(f"Surface Area: {sphere.get_surface_area()}")
print(f"Surface Count: {sphere.get_surface_count()}\n")

# Instantiate 20 cubes
cube = Cube("red", 0, 0, 0, 5)

# Print cube properties
print(f"Cube:")
print(f"Coordinates: {cube.get_center()}")
print(f"Color: {cube.color}")
print(f"2D Area: {cube.get_cross_section_area()}")
print(f"2D Perimeter: {cube.get_cross_section_perimeter()}")
print(f"3D Volume: {cube.get_volume()}")
print(f"Surface Area: {cube.get_surface_area()}")
print(f"Surface Count: {cube.get_surface_count()}\n")

# Instantiate 20 equilateral triangular bipyramids
base_length = 10
height = 10
bipyramid = TriangularPyramid("yellow", 20, 0, 20, base_length, height)

# Print bipyramid properties
print(f"Bipyramid:")
print(f"Coordinates: {bipyramid.get_center()}")
print(f"Color: {bipyramid.color}")
print(f"2D Area: {bipyramid.get_cross_section_area()}")
print(f"2D Perimeter: {bipyramid.get_cross_section_perimeter()}")
print(f"3D Volume: {bipyramid.get_volume()}")
print(f"Surface Area: {bipyramid.get_surface_area()}")
print(f"Surface Count: {bipyramid.get_surface_count()}\n")
