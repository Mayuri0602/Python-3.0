# class A: 
#      def info(self):
#           print("hey")

#      def __gt__(self,x):    # in-built dunder function call nhi hoga
#           print("greater than") 

# a1 = A()
# a2 = A()
# a1 > a2   
# print(a1)          


# Encapsulation :- combining variables and methods together in a single place, called class to define accessibilty

# class A:
#      __salary = 100

# a1 = A()
# print(a1._a__salary)


# class BankAccountDetails:
#       def __init__(self, accno, username, balance):
#          self.accno = accno
#          self.username = username
#          self.balance = 50000


#       def DepositAmount(self, deposit):
#            if deposit > 0:
#                 self.balance += deposit

#       def func(x, y, z):
                

#        acc1 = BankAccountDetails(45674, "Mahi", 6799)
#        print(acc1.accno, acc1.username)


# acc2 = BankAccountDetails(67234, "Sakshi", 80890)
# print(acc2.accno, acc2.username)


class Student:
    def __init__(self, name):
        self.__name = name   # private variable

    def get_name(self):      # public method to access private data
        return self.__name

s = Student("Yash")
print(s.get_name())   # Yash




class Person:
    def _init_(self, name, age):
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