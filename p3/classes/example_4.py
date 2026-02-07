import math
class circle:
    def __init__(self, x):
        self.x = x
    def area(self):
        y = math.pi*(self.x**2)
        print(f"{y:.2f}")

a = int(input())
x = circle(a)
x.area()