def squares(start, stop, step = 1):
    while start<stop:
        yield start**2
        start+=step

a = input().split()
res = squares(int(a[0]), int(a[1]) + 1)
for num in res:
    print(num, end = " ")
