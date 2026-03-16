a = list(map(int, input().split()))
res = list(filter(lambda x: x % 2 == 0, a))

x = True
for i in res:
    if x:
        print(i, end = '')
        x = False
    else:
        print(',', i, sep = '', end = '')
