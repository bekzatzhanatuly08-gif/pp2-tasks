from functools import reduce
a = list(map(int, input().split()))

res = reduce(lambda x, y: x * y, a)
print(res)