a = list(map(int, input().split()))

mx = -10**18
smx = -10**18

for x in a:
    if x > mx:
        smx = mx
        mx = x
    elif x > smx and x != mx:
        smx = x

print(smx)
