a, b = map(int, input().split())
c, d = map(int, input().split())

if max(a, c) <= min(b, d):
    print("YES")
else:
    print("NO")
