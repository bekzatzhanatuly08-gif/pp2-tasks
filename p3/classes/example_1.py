class animals:
    def __init__(self, name, weigh):
        self.name = name
        self.weigh = weigh
    def out(self):
        print("Name of animal: " + self.name, "Weigh of animal: " + str(self.weigh), sep = "\n")

a = input().split()
x = animals(a[0], int(a[1]))
x.out()