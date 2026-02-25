def gen(start, stop, step = 1):
    while stop > start:
        yield stop
        stop-=step

a = int(input())
res = gen(-1, a)
for num in res:
    print(num, end = " ")