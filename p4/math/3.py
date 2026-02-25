import math

n = int(input())
a = int(input())

res = (n*a**2)/4*math.tan(math.pi/n)

print(int(round(res, 2)))
