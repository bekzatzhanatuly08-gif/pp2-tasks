def myFunc(n):
    return lambda a : a * n

x = myFunc(2)
y = myFunc(3)

print(x(12))
print(y(23))