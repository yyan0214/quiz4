from abc import ABC, abstractmethod
import os

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Equi_triangle(shape):
    def __init__(self,side_length,hight) -> None:
        self.side_length = side_length
        self.hight = hight

    def area(self):
        return (self.side_length * self.hight) / 2

    def perimeter(self):
        return (self.side_length * 3)


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

def main():
    equi_triangle = Equi_triangle(7, 4)
    circle = Circle(4)
    
    print("Equilateral triangle area:", equi_triangle.area())
    print("Equilateral triangle perimeter:", equi_triangle.perimeter())
    
    print("Circle area:", circle.area())
    print("Circle perimeter:", circle.perimeter())
    

if __name__=="__main__":
    main()