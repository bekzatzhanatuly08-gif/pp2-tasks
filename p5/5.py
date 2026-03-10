import re

a = input()
res = re.search(r"^a.*b$", a)

if res:
    print("yes")
else:
    print("no")