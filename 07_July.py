# "Decision-Making"
practical = int(input("Enter number 1 : "))
theory = int(input("Enter number 2 : "))
total = practical + theory
if total >= 33:
    print("Pass")
else:
    print("Fail")  

# relational, logical, membership, identity, boolean operators are operators which gives boolean values.   

# Write a program to check whether a number is even or odd.
a = int(input("Enter a number: "))
if (a%2 == 0):
    print("Even number")
else:
    print("Odd number")  


# Write a program to check if a number is a multiple of 5 or not.
n = int(input("Enter a number: "))
if (n%5 == 0):
    print("Multiple of 5")
else: 
    print("Not a multiple of 5")  


# Write a program to check whether which number is greater.
a = int(input("Enter num1: "))        
b = int(input("Enter num2: "))
if (a>b):
    print("a is greater than b")
else:
    print("b is greater than a")  


# Write a program to check whether the number is a multiple of 3 and 5 both.
n = int(input("Enter a number: "))
if (n%3 == 0) and (n%5==0):
    print("Yes")
else: 
    print("No")  


# Write a program where user get discount on the purchase of 2000 and greater otherwise remains the same.
amount  = int(input("Enter the amount: "))
if (amount > 2000):
    amount = amount - amount*0.10
    print("Discounted amount = ", amount)
else: 
    print("Amount = ", amount)    


amount  = int(input("Enter the amount: "))
if (amount > 0 and amount >= 2000):
     new_amount = amount - amount*0.10
     print("Discounted amount = ", new_amount)
elif (amount > 0 and amount < 2000):
     print("Amount = ", amount) 
else: 
     print("Invalid input")        


# Write a program that takes two number as input and operator also and then perform different arithmetic operations.
n1 = float(input("Enter number1 : "))
op = input("Enter any arithmetic operator: ")
n2 = float(input("Enter number2 : "))     
if (op == '+'):
    print("result = ", n1 + n2)
elif (op == '-'):
    print("result = ", n1 - n2)  
elif (op == '*'):
    print("result = ", n1 * n2) 
elif (op == '/'):
    print("result = ", n1/n2)
else:
    print("Not valid")             


# Write a program to check whether the input character is a vowel or consonant.
ch = input("Enter any character: ")
ch = ch.lower()
if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print("Character is a vowel")
else:
    print("Consonant")  


# false, False  
# if false:
#     print("hi")
# elif True:
#     print("bye")    