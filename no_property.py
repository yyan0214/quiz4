class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_size(self):
        return self._length, self._width

    def set_size(self, new_len, new_wid):
        self._length = new_len
        self._width = new_wid
        
    def get_area(self):
        return self._length * self._width

    

# Testing the class
if __name__ == "__main__": 
    rectangle = Rectangle(7,4)
    
    print("The size of the rectangle is:", rectangle.get_size())
    print("Area:", rectangle.get_area())

    rectangle.set_size(8,5)

    print("New size:", rectangle.get_size())
    print("New Area:", rectangle.get_area())
  
