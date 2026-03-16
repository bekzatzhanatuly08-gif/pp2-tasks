import shutil
shutil.copy('sample.txt', 'backup.txt')

with open('backup.txt', 'a') as f:
    f.write('Orange')

with open('backup.txt') as s:
    print(s.read())