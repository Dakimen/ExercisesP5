"""This file contains exercice 9."""


class Rectangle:
    """Rectangle class defining a rectangle with a width and a length.

    Attributes:
    width (int or float): width of the rectangle.
    length (int or float): length of the rectange.

    Methods:
    calculate_area(): Return rectangle's area.
    calculate_perimeter(): Return rectangle's perimeter.
    """

    def __init__(self, width, length):
        """Create rectangle class.

        Args:
        width (int or float): width of the rectangle.
        length (int or float): length of the rectangle
        """
        self.width = width
        self.length = length

    def calculate_area(self):
        """Return rectangle's area (int or float)."""
        return self.width * self.length

    def calculate_perimeter(self):
        """Return rectangle's perimeter (int or float)."""
        return 2 * (self.width + self.length)


# Test de la classe Rectangle
rectangle = Rectangle(5, 3) # 5:width & 3:length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
