a = int(input())
b = list(map(int, input().split()))

res = 0
for i in range(len(b)):
    res+=b[i]**2

print(res)