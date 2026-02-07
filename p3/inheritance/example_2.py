class person:
    def __init__(self, name):
        self.name = name
class student(person):
    def __init__(self, name , gpa):
        super().__init__(name)
        self.gpa = gpa
    def display(self):
        print("Student: " + self.name + "," + " GPA: " + str(self.gpa))

a = input().split()
x = person(a[0])
y = student(a[0], float(a[1]))
y.display()

 