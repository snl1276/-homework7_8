import math
from abc import ABC, abstractmethod


class Point:
    def __init__(self, x =0, y=0) -> float:
        self.x = x
        self.y = y

class Line:
    def __init__(self, a=Point(), b=Point()):
        self.a = a
        self.b = b

    def length(a, b) -> float:
        return math.sqrt((a.x-b.x) ** 2 + (a.y-b.y) ** 2)


class Square(Line):
    
        
    def area(w) -> float:
        return w * w 
    
    
    def perimeter(w)-> float:
        return w * 4 
         
'''
class Cube(Square):
    
    
    def volume(h)-> float:
         V = area.w * h 
         return V
 '''   
    
A = Point(1, 4)
B = Point(6, 4)
C = Point(6, 1)
AB = Line.length(A, B)
BC = Line.length(B, C)
print('AB =', AB)
print('BC =', BC)
print('Площадь квадрата со стороной AB равна', Square.area(AB))
print('Периметр квадрата со стороной AB равен', Square.perimeter(AB))
'''
print('Объем куба со стороной AB равен', Cube.volume(AB))
'''