# Dunder Functions :- Built-in special or magic methods that have names enclosed by double underscores

class A: 
    def __init__(self, x):
        self.x = x

    def __gt__(self, other):   # "greater than" operator
        return self.x > other.x

    def __str__(self):         # to print object nicely
        return f"A(value={self.x})"

a1 = A(10)
a2 = A(5)

print(a1 > a2)   # Calls __gt__ → True
print(a2 > a1)   # Calls __gt__ → False
print(a1)        # Calls __str__ → A(value=10)
print(a2)        # Calls __str__ → A(value=5)



class A: 
     def info(self):
          print("hey")

     def __gt__(self,x):         
          print("greater than") 

a1 = A()
a2 = A()
a1 > a2   
print(a1)          



# Encapsulation :- combining variables and methods together in a single place, called class to define accessibilty

class A:
     __salary = 100          # private attribute

a1 = A()
print(a1._A__salary)         # obj_class__attribute



class Student:
    def __init__(self, name):
        self.__name = name   # private variable

    def get_name(self):      # public method to access private data
        return self.__name

s = Student("Yash")
print(s.get_name())   # Yash




class Person:
    def __init__(self, name, age):
        self.name = name        # Public attribute
        self.__age = age        # Private attribute (encapsulated)

    def get_age(self):
        return self.__age       # Public method to access private data

    def set_age(self, age):
        if age > 0:
            self.__age = age    # Setter with validation

# Usage
p = Person("Alice", 30)
print(p.name)           # Output: Alice
print(p.get_age())      # Output: 30

p.set_age(35)
print(p.get_age())      # Output: 35

# print(p.__age)        # Error: __age is private



# Public members are variables or methods that can be accessed anywhere inside or outside the class or from other modules.
# By default, all members are public in Python.

class Student:
    def __init__(self, name):
        self.name = name   # public variable

    def display(self):     # public method
        print("Name:", self.name)

s1 = Student("Mayuri")
print(s1.name)      # Accessible outside
s1.display()        # Accessible outside




# Protected members are variables or methods that are intended to be accessed only within the class and its subclasses,
# defined with a single underscore prefix

class Student:
    def __init__(self, name, marks):
        self._marks = marks   # protected variable
        self.name = name

    def _display(self):       # protected method
        print("Marks:", self._marks)

class SubStudent(Student):     # subclass
    def show(self):
        print("Accessing protected variable in subclass:", self._marks)

s1 = SubStudent("Mayuri", 90)
print(s1.name)         # Public variable
print(s1._marks)       # Possible but not recommended outside
s1._display()          # Possible but not recommended outside
s1.show()              # Proper way (via subclass)



# Private members cannot be accessed directly from outside the class, they are used to restrict access and protect internal data.
#  defined with a double underscore prefix

class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError


# Note: Unlike other programming languages, Python does not enforce access modifiers like public, private or protected at the language level.
# However, it follows naming conventions and uses a technique called name mangling to support encapsulation.



class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}")  # Protected method

    def __update_balance(self, amount):
        self.balance += amount             # Private method

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance()           # Accessing protected method
        else:
            print("Invalid deposit amount!")
            
account = BankAccount()
account._show_balance()      # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)         # Uses both methods internally




class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)   # Update salary using setter
print(emp.get_salary())