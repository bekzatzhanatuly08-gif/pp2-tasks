import re
a = input()

res = re.search(r"^[a-z]+\_[a-z]+$", a)

if res:
    print("Yes")
else:
    print("No")