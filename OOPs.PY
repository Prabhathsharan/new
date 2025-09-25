#Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Sample Run
animals = [Dog(), Cat()]
for a in animals:
    print(a.sound())
#------------
#Encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name        
        self.__age = age        

    def set_age(self, age):
        if age > 0:
            self.__age = age    

    def get_age(self):
        return self.__age        

p = Person("Alice", 25)
print(p.name)       
print(p.get_age())  

p.set_age(30)
print(p.get_age()) 

#----------
#Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"{self.brand} is moving."

class Car(Vehicle):   
    def drive(self):
        return f"{self.brand} car is driving."

# Sample Run
v = Vehicle("Generic")
c = Car("Tesla")
print(v.drive())   
print(c.drive())   
#------------------
#Polymorphism
class Bird:
    def fly(self):
        return "Some birds can fly."

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high."

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly."

# Sample Run
birds = [Sparrow(), Penguin()]
for b in birds:
    print(b.fly())

