# Nested if-else

# Formatted String:- It is basically used to insert variables or arithmetic operations inside an existing string.  

# Indexing:- Forward, Reverse(starting should be greater than stop)

# Slicing:- It is a technique through which we extract a portion (substring or sublist) from a string.
# (start,stop,step)
# By default, step value '1' rehti hai
data = 'regex software'
print(data[0:6])
print(data[0:16:2])
print(data[::1])
print(data[::-1])
print(data[:-15:-2])

# # Different operations on string:-
name = "dipti keshav"
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.title())
print(name.count('i'))

# Primitive(built-in) datatype like int, float, boolean, strings and 
# Non-primitive(made by using primitive datatype) datatype include lists, tuples, sets, dictionary


email = input("Enter your email id : ")
if (email.endswith('@gmail.com')):
    print("Valid")
else:
    print("Not valid")    



orig_email=input("Enter your email: ")
orig_password=input("Enter your password: ")
print("""
Press 1 for login
Press 2 for exit """) 
choice = int(input("Enter: ")) 
if (choice == 1):
    new_email=input("Verify yor email: ")
    new_password=input("Verify your password: ")
    if (new_email==orig_email and new_password==orig_password):
         print("Login successful")
    else:
          print("Login failed")
elif  (choice == 2):
     print("Exit")
else:
   print("Wrong input")

# split converts the string into list
data = "welcome to regex"
print(data.split())
print(data.split('e'))
print(data.split(" ")[::-1]) 
# joins elements of a list into a single string
print(("").join(data))

print(data.index('e'))  
# returns the index of the first occurence of the character 'e'

a = 'school'
b = 'abc123'
c= '1234'
print(len(a))
print(a.isalnum())
print(c.isalnum())
print(b.isalpha())
print(c.isnumeric())

# ASCII 
d = 65
print(chr(d))

e = 90
print(chr(e))

f = 97
print(chr(f))

g = 122
print(chr(g))




