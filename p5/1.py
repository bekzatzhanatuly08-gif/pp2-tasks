import re
a = input()

res = re.search(r"^ab*$", a)

if res:
    print("Yes")
else:
    print("No")