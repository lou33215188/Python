import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, x, y):
        x.x = 2
        y.x = 1


A = Point(0, 0)
B = Point(3, 4)
C = Line(A, B)
print(A.x)
print(B.x)
