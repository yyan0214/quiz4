from typing import Protocol
import os


class shape(Protocol):
    def area(self) -> float:
        pass
    
    def perimeter(self) -> float:
        pass

class Equi_triangle:
    def __init__(self, side_length: float, height: float):
        self.side_length = side_length
        self.height = height
    
    def area(self) -> float:
        return (self.side_length * self.height) / 2
    
    def perimeter(self) -> float:
        return (self.side_length * 3)
    
class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14 * self.radius * self.radius
    
    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius

# Testing the classes
if __name__ == "__main__":
    equi_triangle = Equi_triangle(8, 4)
    circle = Circle(6)
    
    print("Equilateral triangle area:", equi_triangle.area())
    print("Equilateral triangle perimeter:", equi_triangle.perimeter())
    
    print("Circle area:", circle.area())
    print("Circle perimeter:", circle.perimeter())
