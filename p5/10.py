import re

a = input()
res = re.sub(r"(?<!^)([A-Z])", r"_\1", a)
print(res.lower())