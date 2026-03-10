import re
a = input()

res = re.split(r"(?=[A-Z])", a)
for i in res:
    if len(i) == 0:
        res.remove(i)

print(res)