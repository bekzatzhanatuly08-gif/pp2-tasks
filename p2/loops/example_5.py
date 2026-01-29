a = input().split()

used = []

for x in a:
    if x not in used:
        used.append(x)
        cnt = 0
        for y in a:
            if y == x:
                cnt += 1
        print(x, cnt)
