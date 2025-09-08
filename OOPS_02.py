# We need 'self' to differentiate between instance variables (object-level) and local variables (inside a method).

class Student:
    def __init__(name, age):   # ❌ forgot self
        name = name
        age = age

# s1 = Student("Mayuri", 21)
# print(s1.name)               Error



class Student:
    def __init__(self, name, age):   # ✅ use self
        self.name = name
        self.age = age

s1 = Student("Mayuri", 21)
s2 = Student("Yash", 22)

print(s1.name, s1.age)   # Mayuri 21
print(s2.name, s2.age)   # Yash 22



class HouseDesign:
      color = "white"

h1 = HouseDesign()
print(h1.color)         # white
h1.color = "yellow"
print(h1.color)         # yellow



class HouseDesign:
    def __init__(self, a):
        print("constructor called", a)

x = HouseDesign("brown")            # x is a variable or object  



class HouseDesign:
    def __init__(self):
        print("constructor called", self)      # Self is a variable that stores reference of the current object

x = HouseDesign()
print(x)                                       # memory address are the same

# "self" can be changed with any other variable also. 


class HouseDesign:
     def __init__(self, hcolor):
         self.color = hcolor            # instance variable is a var. that is associated with the current object(self)

h1 = HouseDesign("white")
print(h1.color)




class HouseDesign:
     def __init__(self, hcolor, price):
         self.color = hcolor            # instance variable = local variable
         self.price = price             # If the value of a variable varies from object to object, then such variables are called instance variables.

     def houseInfo(self):
         print("House information", self.color, self.price)

house1 = HouseDesign("black",60000)
house1.houseInfo()            

house2 = HouseDesign("white",90000)
house2.houseInfo()            




class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Name:', stud.name, 'Age:', stud.age)

# create object
stud = Student("Jessa", 20)

# call instance method
stud.show()




# Inheritance :- where we inherit members or property of one class into another (reusability is the imp. feature of inheritence)

class A:                      # Parent class/ Super class/ Base class
      amount = 500

# child class(parentclass)
class B(A):                   # Child class/ Sub class/ Derived class
      salary = 1000

# object of class B
b1 = B()
print(b1.amount)        # can access parent class(A) because child class inherit parent class




class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Teacher(Student):
    def __init__(self, tname, temail):
        super().__init__(tname, temail)         # parent class constructor called

# "Super" is a keyword used to access function or property of parent class into child class

# Constructor Chaining:- calling one constructor from another constructor, 
# ensures that all parent class constructors are executed when an object is created

t1 = Teacher("aditya", "aditya344@gmail.com")
print(t1.email)

t2 = Teacher("naina", "naina8656@gmail.com")
print(t2.name, t2.email)




# Multilevel Inheritence :- a chain of inheritence   (grandparent --->  parent --->  child)
class A:
     num1 = 2

class B(A):
      num2 = 6 

class C(B):
      num3 = 9

a1 = A()
print(a1.num1)
# print(a1.num2)
# print(a1.num3)

b1 = B()
print(b1.num1)
print(b1.num2)
# print(b1.num3)


c1 = C()
print(c1.num1)
print(c1.num2)
print(c1.num3)



