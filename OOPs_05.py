# Encapsulation example

class BankAccount:
    __charge = 50      

    def __init__(self, username, balance):
        self.username = username
        self.__balance = balance

    def withdraw(self, amount):
        new_amount = amount + self.__charge       # __charge
        if new_amount <= self.__balance:
            self.__balance -= new_amount 

    def display(self):
        print(f"The balance is: {self.__balance}")

obj1 = BankAccount("mahi", 6000) 
print(f"Before withdrawing the balance: ")
obj1.display()                  

obj1.withdraw(500)
print(f"After withdrawing, the balance is: ")
obj1.display()

# Method Resolution Order in Multi-level Inheritance
# Name mangling is the process Python uses to change the name of private variables (variables starting with __)
# internally to avoid accidental access from outside the class.

class Parent:
    def display(self):
        print("This is parent class")

class Child(Parent):
    def display(self):
        print("This is parent class")

class Grandchild(Child):
    def display(self):
        print("This is grandchild class")

class GreatGrandchild(Grandchild,Child):
    def display(self):
        print("This is greatgrandchild class")


g = GreatGrandchild()
g.display()
print(GreatGrandchild.mro())     # mro:- method resolution order



# Abstraction :- It is a feature of OOP in which we hide internal(implementation) details and show only the required functionalities, 
#                implemented using Abstract Base Classes and abstract methods from the 'abc' module

# Hides implementation details from the user.
# Provides a blueprint for subclasses.
# Forces subclasses to implement essential methods.
# Abstract classes can have __init__() constructors.
# Subclasses can call them using super() to initialize common properties.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_vehicle(self):
        pass

class Bike(Vehicle):
    def start_vehicle(self):
        print("The bike is started with key")

class Car(Vehicle):
    def start_vehicle(self):
        print("The car starts with key")

c = Car()
c.start_vehicle()

b = Bike()
b.start_vehicle()




from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def area(self, length, breadth):
        return length * breadth
    
rect = rectangle()
area = rect.area(10, 15)
print(area)    

class square(shape):
    def area(self, side):
        return side * side

sq = square()
area = sq.area(10)
print(area)  




# Online Payment System
from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def payment_initialize(self, amount):
        pass

    @abstractmethod
    def payment_process(self, amount):
        pass

    @abstractmethod
    def payment_status(self):
        pass

class UPI(PaymentSystem):
    def payment_initialize(self, amount):
        print(f"The initialized payment is: {amount}")

    def payment_process(self, amount):
        print("payment is processing")

    def payment_status(self):
        print("payment has been completed")

upi = UPI()
upi.payment_initialize(5000)
upi.payment_process(5000)
upi.payment_status()


class CreditCard(PaymentSystem):
    def payment_initialize(self, amount):
        print(f"The initialized payment is: {amount}")

    def payment_process(self, amount):
        print("Payment is processing !")

    def payment_status(self):
        print("Payment has been completed !")

cc = CreditCard()
cc.payment_initialize(9000)
cc.payment_process(9000)
cc.payment_status()

