a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
for i, j in zip(a, b):
    res+=i*j

print(res)