# create an abstract class Shape with abstract methods get_area() and get_perimeter()
# create two subclasses
# -Rectangle
# -Square
# -Each class should calculate area() and perimeter() differently.

from abc import ABC,abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def get_area(self):
        pass
    
    @abstractmethod
    def get_perimeter(self):
        pass    
    
class Rectangle(Shape):
    
    def __init__(self):
        print("Enter the rectangle details")
        self.length=int(input("Enter the length :"))
        self.breadth=int(input("Enter the breadth :"))
        
    def get_area(self):
        print("Area =",self.length*self.breadth)
        
    def get_perimeter(self):
        print("Perimeter =",2*(self.length+self.breadth))
        
class Square(Shape):
    
    def __init__(self):
        print("Enter the square details")
        self.side=int(input("Enter the length of the side :"))
        
    def get_area(self):
        print("Area =",self.side**2)
        
    def get_perimeter(self):
        print("Perimeter =",self.side*4)
        
r = Rectangle()
r.get_area()
r.get_perimeter()

s = Square()
s.get_area()
s.get_perimeter()