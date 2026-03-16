with open('sample.txt', 'w') as f:
    f.write('Apple\n')
    f.write('Banana\n')
    f.write('Cherry\n')

with open('sample.txt') as s:
    print(s.read())