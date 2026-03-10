import re

a = input()
res = re.search(r"^ab{2,3}$", a)

if res:
    print("Yes")
else:
    print("No")