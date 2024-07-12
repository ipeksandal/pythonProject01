import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distance_to(self, point):
        return math.sqrt((self.x - point.getx())**2 + (self.y - point.gety())**2)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3

    def perimeter(self):
        side1 = self.vertice1.distance_to(self.vertice2)
        side2 = self.vertice2.distance_to(self.vertice3)
        side3 = self.vertice3.distance_to(self.vertice1)
        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
