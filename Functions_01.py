# Functionn is a reusable block of code that performs a specific task and makes the code more readable.

# Parameters are the variables passing at the time of defining a function.

# Arguments are the values passing at the time of calling a function.


def maximum(a,b):
    if a>b:
        print(a)
    else:
        print(b)
maximum(10,90)  
          



def mul():
    a=int(input(("n1: ")))
    b=int(input("n2: "))
    print(a*b)
mul()    




def display():
    a=int(input("n1: "))
    b=int(input("n2: "))
    c=input("Enter your choice: + or *: ")
    if c=='+':
        print(a+b)
    else:
        print(a*b)
display()   
         



def display():
    a=int(input("n1: "))
    b=int(input("n2: "))
    c=input("Enter your choice: + or *: ")
    if c=='+':
        print(a+b)
    else:
        print(a*b)
while True:
     display()   
     choice= input("Press 1 for more calculations or 0 to stop: ")
     if choice=='0':
         break



# Function with parameter and without return
def add(a,b):
    print(a+b)
add(10,90)


# Function with parameter and return
def sub(a,b):
    return(a-b)
print(sub(100,90))


# Function without parameter and return
def mul():
    return (10*10)
print(mul())


# Function without parameter and without return
def div():
    print(100//10)
div()     



# Return is a keyword used to end the execution of the function call and returns the value of the expression. (any variable or expression can be used)
# If we want to display the return value then we have to call the function with print() function.
# The statements after the return statements are not executed. If the return statement is without any expression, then the special value "None" is returned.

def cube(a):
    return (a**3)

cube(3)              # output show nahi hoga
print(cube(5))       # 125



# Default value is the value we stored in parameter so that if we don't pass the value in argument, it will work as an argument.

def greet(name="admin"):
    return ("Hello, " + name + " !")

print(greet())
print(greet("user"))

