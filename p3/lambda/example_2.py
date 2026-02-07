a = int(input())
b = input().split()
l = []
for i in range(a):
    l.append(int(b[i]))

res = list(map(lambda x: x**2, l))
print(res)