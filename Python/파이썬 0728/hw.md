1. Circle 인스턴스 만들기
    아래와 같은 Circle 클래스가 있을 때, 반지름이 3이고 x, y좌표가 (2, 4)인
    Circle 인스턴스를 만들어 넓이와 둘레를 출력하시오
```
class Circle:
    pi = 3.14
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    def area(self):
        return Circle.pi * self.r * self.r
    
    def circumference(self):
        return 2 * Circle.pi * self.r
    
    def center(self):
        return (self.x, self.y)



c1=Circle(3,2,4) 
print(c1.area()) #28.25999999
print(c1.circumference()) #18.84

```

2. Dog과 Bird는 Animal이다
    다음과 같이 Animal 클래스가 주어질 때, 해당 클래스를 상속 받아 아래의 보기와 같이
    동작하는 Dog 클래스와 Bird 클래스를 작성하시오.

```
class Animal:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(f'{self.name}! 걷는다!')
    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def run(self):
        print(f'{self.name}! 달린다!')
    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')


dog = Dog('꼽이')
dog.run() # 꼽이! 달린다! 
dog.bark() # 꼽이! 짖는다!
bird = Bird('구구')
bird.walk() # 구구! 걷는다! 
bird.eat() # 구구! 먹는다! 
bird.fly() # 구구! 푸드덕!        
```    

3. Module Import
```
# fibo.py
def fibo_recursion(n):
if n < 2:
return n
else:
return fibo_recursion(n-1) + fibo_recursion(n-2)

from __(a)__ import __(b)__ as __(c)__
recursion(4)
```

a = fibo.py b = fibo_recursion c = recursion