import re

a = input()
res = re.sub(r"(?<!^)([A-Z])", r" \1", a)
print(res)