from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        area = 0.5*self.dim1*self.dim2
        print('Area of circle ', area)


a = Circle(10, 10)
a.area()
