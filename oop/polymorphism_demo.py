# polymorphism_demo.py
import math

# Base class
class Shape:
    def area(self):
        """Calculate area of the shape. To be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override this method")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle: length × width"""
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of a circle: π × radius²"""
        return math.pi * self.radius ** 2
