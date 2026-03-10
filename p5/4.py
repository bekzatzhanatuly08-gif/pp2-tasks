import re

a = input()
res = re.search(r"^[A-Z][a-z]+", a)

if res:
    print("yes")
else:
    print("no")