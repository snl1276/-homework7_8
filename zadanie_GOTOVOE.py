import math
from abc import ABC, abstractmethod


class Point:
    def __init__(self, x=0, y=0) -> float:
        self.x = x
        self.y = y
    
    
    def print_point(self):
        print('({0}, {1})'.format(self.x, self.y))


class Line:
    def __init__(self, a=Point(), b=Point()):
        self.a = a
        self.b = b

    def length(a, b) -> float:
        return math.sqrt((a.x-b.x) ** 2 + (a.y-b.y) ** 2)


class Shape (ABC):
    
    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass


class Square(Line, Shape):
    
        
    def area(w) -> float:
        return w * w 
    
    
    def perimeter(w) -> float:
        return w * 4 
         
class Cube(Square):
    
    
    def volume(w, h) -> float:
         V = Square.area(w) * h 
         return V


class Rect(Shape):
    
    def __init__(self, storona1, storona2):
        self.storona1 = storona1 or Line()
        self.storona2 = storona2 or Line()
        
    def area(storona1, storona2) -> float:
        return storona1 * storona2
    
    
    def perimeter(storona1, storona2) -> float:
        return (storona1 + storona2) * 2 


A = Point(1, 4)
print('Координаты точки А:')
A.print_point()
B = Point(6, 4)
print('Координаты точки B:')
B.print_point()
C = Point(6, 1)
print('Координаты точки C:')
C.print_point()
AB = Line.length(A, B)
BC = Line.length(B, C)
print('AB =', AB)
print('BC =', BC)
print('Площадь квадрата со стороной AB равна', Square.area(AB))
print('Периметр квадрата со стороной AB равен', Square.perimeter(AB))

print('Объем куба со стороной AB равен', Cube.volume(AB, AB))

print('Площадь прямоугольника со сторонами AB  и ВС равна', Rect.area(AB, BC))
print('Периметр прямоугольника со сторонами AB и ВС равна', Rect.perimeter(AB, BC))
