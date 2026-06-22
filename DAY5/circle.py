import math
class Circle:
    def __init__(self,r):
        self.rad=r
    def area(self):
        return math.pi*(self.rad)**2
    def perimeter(self):
        return 2*math.pi*self.rad
c=Circle(2)
print(c.area())
print(c.perimeter())