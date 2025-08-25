# lambda function is an anonymous function, don't have a name, one line or inline functions

cube = lambda x: x**3
print(cube(3)) 

a=lambda x: x+24
print(a(34))

a=lambda y: y+20
out= a(35)
print("value of lambda",out)


def func(x):
    print(x+20)
    return [x,x+20]
z = func(80) 
print("value is",z)   #to use the values


# First class Function:- It's like a mechanism or a feature that helps us to write our function in a flexible and reusable manner.
# Characteristics are - assigned to variables, passed as arguments, function can return other function

def tester():
    print("hey")

y = tester()       # y will have return value of function
z = tester         # z will have memory of function

print("y value:",y)             # y value = None because return use nhi kiya
print("tester: ",tester,z)



def Square(n):
    print(n ** 2)

out = Square(9)    # 81
print(out)         # returns None value because return nhi kiya