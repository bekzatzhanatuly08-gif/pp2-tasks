import re
a = input()

res = re.sub(r"[ ,.]", r":", a)
print(res)
