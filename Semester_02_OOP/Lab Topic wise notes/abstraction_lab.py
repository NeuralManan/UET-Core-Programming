from abc import ABC, abstractmethod

# abstract class   (whenever we define abstarct class using this abstract method it will be the child of ABC allways)

class Shape(ABC):

    @abstractmethod
    def area(self):
        # Abstract method to calculate area,   must be implemented by all the subclasses.  otherwise there will be error
        pass

    @abstractmethod
    def perimeter(self):
        # Abstract method to calculate perimeter,   must be implemented by all the subclasses.  otherwise there will be error
        pass

#object = Shape()    #TypeError: Can't instantiate abstract class Shape without an implementation for abstract methods 'area', 'perimeter'


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # def area(self):
    #     return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)  
    
rec1 = Rectangle(2, 4)
# print(rec1.area())   when we comment or hide it TypeError: Can't instantiate abstract class Rectangle without an implementation for abstract method 'area'
print(rec1.perimeter())






