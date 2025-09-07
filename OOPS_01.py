# OOPS Object Oriented Programming System is a concept of programming where everything is treated as objects.

# Why we need OOPs ?
# We need OOP because it helps us write organized, reusable, secure, and scalable code — especially in large projects.

# object :- real world entity that has its characteristics(apperance) and behaviour(functionality)
# example:- student is an object, sname/email are characteristics and course_name is behaviour

# class :- is a blue print and template for the object (store methods and attributes together in a single unit)
# example:- admission card


class AdmissionForm:
    name = "yash"
    course = "B.Tech"                    # attributes (variables)


# student is object here
student1 = AdmissionForm( )              # object = class()
print(student1.course)

student1.course = "BCA"                  # change for obj. Student1 only
print("Updated", student1.course)        # whenever changes are done for the object, it will be for that particular object only

stud2 = AdmissionForm()                  # object 2
print("Student2",stud2.course)


# To do the same work of print again & again, we use method/function to call it 

class AdmissionForm:
     name = "yash"
     course = "B.Tech"

     def info(self):                                 # method :- info
        print("My name is: ",self.name)
        print("My course name is: ",self.course)

stud = AdmissionForm()
stud.info()  

stud2 = AdmissionForm()
stud2.info()

stud = AdmissionForm()
stud.name = "Mayu"             # only for this object 
stud.info()

AdmissionForm.name = "REgex"   # whenever we defined a variable inside a class is called class variable, can be accessed by class and object name 
print(AdmissionForm.name)



class AdmissionForm:
     name = "yash"
     course = "B.Tech"

print("before",AdmissionForm.name)

AdmissionForm.name = "REgex"        # changes made with class is visible for every object
print("after:",AdmissionForm.name)  # now all objects (existing and new) would see "REgex" unless they had their own obj. attribute.

stud = AdmissionForm()
print(stud.name)




class Person:
      pname = "mayank"
      pemail = "mayank15@gmail.com"
      pid = "22"

      def details(self):
          print("My name is: ",self.pname)
          print("Mail id is: ",self.pemail)
          print("Id is: ",self.pid)

person1 = Person()
person1.details()          



# Constructor:- method or a function used to initialize memory address for the object
# It is a special method __init__() inside a class that automatically runs when an object is created

class AdmissionForm:
      def __init__(self):             #syntax for constructor
            print("Called constructor")


AdmissionForm()                      # calling the constructor
x = AdmissionForm()                  # stored in a variable, x to print its return value, i.e., memory address for the object
print("Return from constructor: ",x) # it gives new memory address every time for the object           


# Self is a variable that stores reference of current object.
# Self keyword can be changed with any other variable.
 