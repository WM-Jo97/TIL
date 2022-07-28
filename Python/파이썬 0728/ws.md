1. 도형 만들기
    아래의 명세를 읽고 Python 클래스를 활용하여 점(Point)과 사각형(Rectangle)을
    표현하시오


```
class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y

class Rectangle(Point):
    def __init__(self, p1, p2):
        self.p1=p1
        self.p2=p2

    def get_area(self):
        self.LX=abs(self.p1.x-self.p2.x)
        self.LY=abs(self.p1.y-self.p2.y)
        area=self.LX*self.LY
        return area

    def get_perimeter(self):
        ALX=abs(self.p1.x - self.p2.x)
        ALY=abs(self.p1.y - self.p2.y)
        perme=2*ALX+2*ALY
        return perme

    def is_square(self):
        if self.LX==self.LY:
            return True
        else:
            return False

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
```