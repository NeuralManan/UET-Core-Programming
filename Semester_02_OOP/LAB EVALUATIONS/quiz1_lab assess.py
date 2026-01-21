class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius 

    @classmethod
    def setPi(cls, value):
        cls.pi = value
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        try:
            if value < 0:
                raise ValueError("Radius cannot be negative")
            self._radius = value
        except ValueError:
            self._radius = abs(value)
    def getArea(self):
        area = Circle.pi * (self.radius ** 3)
        print("Area of Circle:", area)

c = Circle(5)
c.getArea()
Circle.setPi(100)
print(Circle.pi)


