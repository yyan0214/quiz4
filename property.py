class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, num):
        if num <= 0:
            raise ValueError("Length must be positive")
        self._length = num

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, num):
        if num <= 0:
            raise ValueError("width must be positive")
        self._width = num

    @property
    def area(self):
        return self._length * self._width

    

# Testing the class
if __name__ == "__main__": 
    rectangle = Rectangle(7,4)
    
    print("Length:", rectangle.length)
    print("Width:", rectangle.width)
    print("Area:", rectangle.area)

    rectangle.length = 8
    rectangle.width = 5
    print("\nNew length:", rectangle.length)
    print("New width:", rectangle.width)
    print("New Area:", rectangle.area)
  
