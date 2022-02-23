class Point(object):
    def __init__(self, x: float, y: float) -> float:
        self.x = x
        self.y = y

    def Line(self, other):
        length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return length
    #def Rect(self,):
        
    
p1_x = float(input("p1.x: "))
p1_y = float(input("p1.y: "))

p2_x = float(input("p2.x: "))
p2_y = float(input("p2.y: "))

p3_x = float(input("p3.x: "))
p3_y = float(input("p3.y: "))

p4_x = float(input("p4.x: "))
p4_y = float(input("p4.y: "))

p1 = Point(p1_x, p1_y)
p2 = Point(p2_x, p2_y)
p3 = Point(p3_x, p3_y)
p4 = Point(p4_x, p4_y)

print(p1.Line(p2))
print(p2.Line(p3))
print(p3.Line(p4))
print(p1.Line(p4))
