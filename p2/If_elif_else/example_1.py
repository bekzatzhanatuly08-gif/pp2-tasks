a, b, c = map(int, input().split())

if a + b <= c or a + c <= b or b + c <= a:
    print("NO")
elif a == b == c:
    print("EQUILATERAL")
elif a == b or a == c or b == c:
    print("ISOSCELES")
else:
    print("SCALENE")
