#-----------creating class and object---------------
# class Student:
#     pass
# s1 = Student()

#-----------creating class and object with attributes---------------
# class Student:
#     def __init__(self, name, age):  #self is a reference to the current instance of the class, it is used to access the attributes and methods of the class
#         self.name = name
#         self.age = age
        
# s1 = Student("Pravin" , 25)
# print(s1.name)
# print(s1.age)

#-----------creating class and object with attributes and method---------------
# class Student:
#     def __init__(self, name): #__init__ is a constructor method that is called when an object is created, it is used to initialize the attributes of the class
#         self.name = name

#     def speak(self):
#         print(f"{self.name} is speaking")
        
# s1 = Student("Pravin")  
# s1.speak()

#-----------creating class and object with encapsulation---------------
# class Bank:
#     def __init__(self, balance):
#         self.__balance = balance   # private

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# b = Bank(1000)
# b.deposit(500)
# print(b.get_balance())   #can access balance through method
# print(b.__balance)   #cannot access balance directly, will raise an error

#-----------creating class and object with inheritance(reuse)---------------
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal): # Dog class inherits from Animal class
    def bark(self):
        print("Barking")

d = Dog()
d.eat()
d.bark()

#-------------creating class and object with polymorphism---------------
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in (Dog(), Cat()): #animals is a list of Dog and Cat objects
    animal.sound()

#-------------creating class and object with abstraction---------------
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

c = Car()
c.start()

