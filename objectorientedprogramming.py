#Class: dog
#Properties: name, age, breed
#Method: bark, eat, sleep

#Object 1, 2, 3...
#Properties: fido, 5, german shepherd 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

p1 = Person("sid", 22)
print(p1.getAge())  # Output: 22

