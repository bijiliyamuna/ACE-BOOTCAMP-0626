import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.rad=r
    def area(self):
        return math.pi*(self.rad)**2
    def perimeter(self):
        return 2*math.pi*self.rad
class Triangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return (1/2)*self.a*self.b
    def perimeter(self):
        pass
class Square(Shape):
    def __init__(self,a):
        self.side=a
    def area(self):
        return self.side**2
    def perimeter(self):
        return 4*(self.side)
c=Circle(2)
print(c.area())
print(c.perimeter())
s=Square(2)
print(s.area())
print(s.perimeter())
t=Triangle(2,4)
print(t.area())

