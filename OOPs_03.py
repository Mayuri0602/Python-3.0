# Polymorphism :- Means many forms, same function or operator behaves differently depending on the context,
#                 makes code more flexible and reusable

# Example :- Polymorphism means same interface like power button, but different behavior based on device (object) like TV, AC, etc.

# Types of Polymorphism :- Compile-time(Method Overloading) and Run-time(Overriding)

# Compile-time polymorphism means deciding which method or operation to run during compilation, usually through method or operator overloading but
# Python is dynamically-typed so true method overloading doesn't support in python. 

# Method Overloading :-  In a class, multiple methods with same name but different parameters, the last definition overwrites the previous one
# because of its namespace implementation. Function names are keys in the namespace dictionary, so redefining the same name overwrites the previous one.
# But we can achieve method overloading in python using variable - length argument.

# Operator Overloading

class A:
     def __init__(self, x, y):
          self.x = x
          self.y = y
          
     def __add__(self,z):
          print("+ operator")

a1 = A(10,20)
a2 = A(11,33)
a1 + a2


# Run-time Polymorphism means that the behavior of a method is decided while program is running, based on the object calling it.          
# Method Overriding is a technique to achieve polymorphism (Inheriatance should be there and same class mein override nahi hota) 
# It occurs when a child class defines a method with the same name and parameters as a method in its parent class.
# The child class method replaces (overrides) the parent class method when called from a child object.

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())           

# output:- Bark
#          Meow
#          Some generic sound


# Method overriding happens when a child class defines a method with the same name and parameters as the parent class.
# At runtime, the child’s method is executed instead of the parent’s. We often use super() when we want to extend, 
# not completely replace, parent functionality


class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")
        super().greet()   # call Parent version too

c = Child()
c.greet()
