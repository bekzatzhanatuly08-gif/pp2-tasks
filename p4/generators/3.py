def gen(start, stop, step = 1):
    while start < stop:
        if start % 3 == 0 and start % 4 == 0:
            yield start
        start+=step

a = int(input())
res = gen(0, a+1)
for num in res:
    print(num , end = " ")