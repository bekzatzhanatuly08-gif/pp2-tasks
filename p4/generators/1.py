def gen(start, stop, step = 1):
    while start < stop:
        yield start**2
        start+=step

res = gen(1, 5)
for i in res:
    print(i, end = " ")