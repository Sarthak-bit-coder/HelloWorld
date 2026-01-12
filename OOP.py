# Object-Oriented Programming (OOP) Concepts =
# Classes and Objects
# Inheritance
# Polymorphism
# Encapsulation
############################################################################

from abc import ABC, abstractmethod
wheels = 4  # Class variable shared by all instances of the class


class Car:  # Can import class from another file

    def __init__(self, make, model, year, color):  # Constructor method is __init__
        self.make = make  # Instance variables
        self.model = model  # Instance variables
        self.year = year  # Instance variables
        self.color = color  # Instance variables

    def drive(self):
        print("This " + self.model + " is driving.")

    def stop(self):
        print("This " + self.model + " has stopped.")


# Creating an object (instance) of the Car class

car_1 = Car("Toyota", "Camry", 2020, "Blue")
car_2 = Car("Nissan", "Skyline", 2021, "Silver")

print(car_1.make)  # Accessing attributes
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()  # Calling methods
car_1.stop()


# Inheritance
##################################

class Animal:

    alive = True  # Class variable

    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")


class Rabbit(Animal):  # Inheriting from Animal class

    def run(self):
        print("The rabbit is running.")


class Fish(Animal):  # Inheriting from Animal class

    def swim(self):
        print("The fish is swimming.")


class Eagle(Animal):  # Inheriting from Animal class

    def fly(self):
        print("The eagle is flying.")


rabbit = Rabbit()
fish = Fish()
eagle = Eagle()

# multiple inherited methods = when a class inherits methods from a parent class
###################################################################################################


class Organism:

    alive = True


class Animals(Organism):

    def breathe(self):
        print("This animal is breathing.")


class Dog(Animals):

    def bark(self):
        print("The dog is barking.")


# Multiple Inheritance = when a class inherits from more than one parent class
########################################################################################

class Prey:

    def flee(self):
        print("This animal is fleeing.")


class Predator:

    def hunt(self):
        print("This animal is hunting.")


class Fish(Prey, Predator):  # Inheriting from both Prey and Predator classes

    def hunt(self):  # Overriding the hunt method
        print("The fish is hunting in the water.")

# Super() Function = used to call a method from a parent class
########################################################################################


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)  # Calling the parent class constructor

    def area(self):
        return self.length * self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)  # Calling the parent class constructor
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


# Prevent a user from creatingan object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class that contains one or more abstract methods
# abstract method = a method that is declared, but contains no implementation
#############################################################################################################################


class Vehicle(ABC):  # Making it an abstract class

    @abstractmethod
    def go(self):  # Abstract method
        pass


class Car(Vehicle):
    def go(self):  # Need to override the abstract method
        print("The car is driving.")


class Motorcycle(Vehicle):
    def go(self):
        print("The motorcycle is driving.")


car = Car()
motorcycle = Motorcycle()
vehicle = Vehicle()

car.go()
motorcycle.go()
# vehicle.go()  # This will raise an error since Vehicle is an abstract class

# Pass objects as arguments
############################################


class Car:

    color = None


def change_color(car, color):
    car.color = color


my_car = Car()
change_color(my_car, "Red")
print(my_car.color)  # Output: Red

# Duck Typing = concept where the class of an object is less important than the methods it defines
#               class type is not checked when calling methods/attributes
####################################################################################################################################


class Duck:

    def walk(self):
        print("The duck is walking.")

    def talk(self):
        print("The duck is quacking.")


class Chicken:

    def walk(self):
        print("The chicken is walking.")

    def talk(self):
        print("The chicken is clucking.")


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()


chicken = Chicken()
duck = Duck()
person = Person()

# person.catch(duck)  # Works because Duck has walk and talk methods
person.catch(chicken)  # Works because Chicken has walk and talk methods
