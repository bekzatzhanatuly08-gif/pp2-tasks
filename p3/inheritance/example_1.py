class animal:
    def __init__(self, name):
        self.name = name
class last(animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound
    def res(self):
        print("Name of animal: " + self.name, "Sound of animal: " + self.sound, sep = '\n')

a = input().split()
x = last(a[0], a[1])
x.res()