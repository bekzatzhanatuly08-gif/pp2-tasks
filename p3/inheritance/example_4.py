class Animal:
    def speak(self):
        print("I am animal")

class Dog(Animal):  
    def bark(self):
        print("Gaf!")

d = Dog()
d.speak() 
d.bark()   
