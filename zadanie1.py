import math


class Point:
    def __init__(self, x: float, y: float) -> float:
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def length(self, Point):
        self.length = math.sqrt((Point.x-self.a) ** 2 + (Point.y - self.b) ** 2)
        return self.length
      
       
class Square (Line):
   
    def area(self, w, h):
        return self.length.w * self.length.h    
        
    
p1 = Point(1, 4)
p2 = Line(6, 4)
p3 = Point(1, 1)
p4 = Line(1, 4)
a = p2.length(p1)
b = p4.length(p3)

print(a)
print(b)


