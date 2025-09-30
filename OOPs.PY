#-------------------------
# Abstraction Example
#-------------------------
from abc import ABC, abstractmethod   # Import tools to make abstract classes

class Animal(ABC):                    # Animal is an abstract (base) class
    @abstractmethod                   # abstractmethod means: must be defined in child class
    def sound(self):
        pass                          # no code here, just a rule

class Dog(Animal):                    # Dog inherits from Animal
    def sound(self):                  # Dog gives its own version of sound
        return "Woof!"

class Cat(Animal):                    # Cat also inherits from Animal
    def sound(self):                  # Cat gives its own version of sound
        return "Meow!"

# Sample Run
animals = [Dog(), Cat()]              # Make a list with Dog and Cat objects
for a in animals:                     # Go through each animal
    print(a.sound())                  # Call the sound() of that animal


#-------------------------
# Encapsulation Example
#-------------------------
class Person:
    def __init__(self, name, age):    # constructor (runs when we create a Person)
        self.name = name              # name is public (anyone can see/change)
        self.__age = age              # __age is private (hidden from outside)

    def set_age(self, age):           # method to safely change age
        if age > 0:                   # only if the new age is greater than 0
            self.__age = age          # update age

    def get_age(self):                # method to safely get age
        return self.__age

p = Person("Alice", 25)               # make a person object with name "Alice" and age 25
print(p.name)                         # print Alice’s name
print(p.get_age())                    # print Alice’s age (25)

p.set_age(30)                         # change Alice’s age to 30
print(p.get_age())                    # print the new age (30)


#-------------------------
# Inheritance Example
#-------------------------
class Vehicle:                        # Base class Vehicle
    def __init__(self, brand):        # constructor, takes brand name
        self.brand = brand

    def drive(self):                  # general drive method
        return f"{self.brand} is moving."

class Car(Vehicle):                   # Car is a child class of Vehicle
    def drive(self):                  # Car changes (overrides) the drive method
        return f"{self.brand} car is driving."

# Sample Run
v = Vehicle("Generic")                # make a Vehicle object
c = Car("Tesla")                      # make a Car object
print(v.drive())                      # call Vehicle’s drive
print(c.drive())                      # call Car’s drive (different output)


#-------------------------
# Polymorphism Example
#-------------------------
class Bird:                           # Base class Bird
    def fly(self):                    # general fly method
        return "Some birds can fly."

class Sparrow(Bird):                  # Sparrow is a Bird
    def fly(self):                    # Sparrow gives its own fly method
        return "Sparrow flies high."

class Penguin(Bird):                  # Penguin is also a Bird
    def fly(self):                    # Penguin changes fly method
        return "Penguins cannot fly."

# Sample Run
birds = [Sparrow(), Penguin()]        # make list with Sparrow and Penguin
for b in birds:                       # go through each bird
    print(b.fly())                    # call their fly() method (different results)
