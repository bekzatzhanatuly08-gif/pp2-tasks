def gen(start, stop, step = 1):
    while start < stop:
        if start % 2 == 0:
            yield start
        start += step

a = int(input())
res = gen(0, a+1)
y = True
for num in res:
    if y:
        print(num, end = "")
        y = False
    else:
        print(",", num, sep = "", end = "")

        