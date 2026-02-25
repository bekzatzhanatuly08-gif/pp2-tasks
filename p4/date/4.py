from datetime import datetime
a = input().strip()
b = input().strip()

d1 = datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime(b, "%Y-%m-%d %H:%M:%S")

res = d1-d2
print(res.total_seconds())