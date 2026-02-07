add = lambda x, y: x+y
multiply = lambda x, y: x*y

a = input().split()
print(f"{add(int(a[0]), int(a[1]))}")
print(f"{multiply(int(a[0]), int(a[1]))}")