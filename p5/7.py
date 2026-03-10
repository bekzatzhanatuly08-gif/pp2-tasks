import re

s = input()
res = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

print(res)