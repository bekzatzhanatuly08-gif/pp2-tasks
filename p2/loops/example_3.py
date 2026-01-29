max_val = -10**18

while True:
    x = int(input())
    if x == 0:
        break
    if x > max_val:
        max_val = x

print(max_val)
