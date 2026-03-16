import os

for i in os.listdir():
    if not i.endswith('txt'):
        print(i)