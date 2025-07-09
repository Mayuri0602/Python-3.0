# Q1. Write a program that takes an integer input from the user and checks whether the number is odd or even.
# i = int(input("Enter an integer: "))
# if (i%2 == 0):
#     print("Even number")
# else:
#     print("Odd number")

# Q2. Write a program that takes three numbers as input and prints the largest of the three. 
# n1 = int(input("Enter number1: "))
# n2 = int(input("Enter number2: "))
# n3 = int(input("Enter number3: "))
# if (n1 > n2) and (n1 > n3):
#     print("n1 is greater than n2 and n3")
# elif (n2 > n3) and (n2 > n1):
#     print("n2 is greater than n1 and n3")
# else:
#     print("n3 is greater than n1 and n2")        

# Q3. Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
# y = int(input("Enter any year: "))
# if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#     print("It's a leap year")
# else:
#     print("It's not a leap year")

# Q4. Write a program that takes a percentage (integer) as input and prints the corresponding grade based on the following criteria:
# >= 90: Grade A
# >= 80: Grade B
# >= 70: Grade C
# >= 60: Grade D
# < 60: Grade F
# p = int(input("Enter your percentage: "))
# if (p >= 90):
#     print("Grade A")
# elif (p >= 80 and p < 90):
#     print("Grade B")
# elif (p >= 70 and p < 80):
#     print("Grade C")
# elif (p >= 60 and p < 70):
#     print("Grade D")
# elif (p < 60):
#     print("Grade F")
# else: 
#     print("Invalid input")  

# Q5. Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.   
# l = input("Enter any letter: ")
# l = l.lower()
# if (l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' ):
#     print("Entered letter is a vowel")
# else:
#     print("Consonant") 

# Q6. Write a basic calculator program that takes two numbers and an operator (+, -, *, /) as input and performs the specified operation. 
# Print the result based on the operation.  
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# op = input("Enter any operator(+, -, *, /): ")
# if (op == '+'):
#     print("a+b =",a+b)
# elif (op == '-'):
#     print("a-b =",a-b)
# elif (op == '*'):
#     print("a*b =",a*b)
# elif (op == '/'):
#     print("a/b =",a/b)
# else:
#     print("Invalid input")

# Q7. Write a program that takes a number as input and checks whether it is positive, negative, or zero.
# n = int(input("Enter any number: "))
# if (n > 0):
#     print("Number is positive")
# elif (n < 0):
#     print("Number is negative")
# else:
#     print("Number is equal to zero")        

# Q8. Write a program that checks if a username and password entered by the user match the pre-set values
# username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print
# "Login Failed".
# username = "admin"
# password = "1234"
# u = input("Enter your username: ")
# p = input("Enter your password: ")
# if (u == username) and (p == password):
#     print("Login Successful")
# else:
#     print("Login Failed")    

# Q9. Write a program that takes three sides of a triangle as input and checks if those sides form a valid triangle. 
# A triangle is valid if the sum of any two sides is greater than the third side.
# Check conditions like a + b > c, b + c > a, and a + c > b. 
# a = float(input("Enter side 1: "))
# b = float(input("Enter side 2: "))
# c = float(input("Enter side 3: "))
# if (a + b > c and b + c > a and a + c > b):
#     print("Valid triangle")
# else:
#     print("Invalid triangle")    

# Q10. Write a program that calculates the Body Mass Index (BMI) based on user input for weight (in kilograms) and height (in meters).
# Then categorize the BMI into:
# Underweight (BMI < 18.5)
# Normal weight (18.5 <= BMI < 24.9)
# Overweight (25 <= BMI < 29.9)
# Obesity (BMI >= 30)
# Use the formula: BMI = weight / (height ** 2)
# w = float(input("Enter your weight (in kg): "))
# h = float(input("Enter your height (in metres): "))
# BMI = w/(h**2)
# if (BMI >= 30):
#     print("Obesity")
# elif (BMI < 18.5):
#     print("Underweight")
# elif (18.5 <= BMI < 24.9):
#     print("Normal weight")
# elif (25 <= BMI < 29.9):
#     print("Overweight")            

# Q11. Write a program that calculates the discount for a product based on its price:
# If price is greater than 1000, discount is 10%
# If price is between 500 and 1000, discount is 5%
# Otherwise, no discount
# Print the final price after applying the discount.
# price = int(input("Enter the price: "))
# if (price > 1000):
#     price = price - (price * 0.10)
#     print("Your total price after 10% discount = ",price)
# elif (500 < price < 1000):
#     price = price - (price * 0.05)
#     print("Your total price after 5% discount = ",price) 
# else:
#     print("Final price = ",price)

# Q12. Write a program that takes the name of a month as input and prints the number of days in that month. Consider leap years for February.
# m = input("Enter the month name: ")
# m = m.lower() or m.title()
# if (m == 'january'):
#     print("31 days")
# elif (m == "february"):
#     print("29 days")
# elif (m == "march"):
#     print("31 days")        
# elif (m == "april"):
#     print("30 days") 
# elif (m == "may"):
#     print("31 days") 
# elif (m == "june"):
#     print("30 days")             
# elif (m == "july"):
#     print("31 days") 
# elif (m == "august"):
#     print("31 days") 
# elif (m == "september"):
#     print("30 days") 
# elif (m == "october"):
#     print("31 days") 
# elif (m == "november"):
#     print("30 days") 
# elif (m == "december"):
#     print("31 days")                     
# else:
#     print("Invalid input")    

# Q13. Write a program that simulates a simple ATM. The user should be able to:
# Check balance
# Deposit money
# Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's choices.
# balance = 4000
# pin = 1234
# print("Welcome to the ATM")
# print("1. Check balance")
# print("2. Deposit money")
# print("3. Withdraw money")
# c = int(input("Enter your choice: "))
# if (c == 1):
#     p = int(input("Enter the pin: "))
#     if (p == pin):
#        print("Your balance: ",balance)
#     else:
#         print("Invalid pin")        
# elif (c == 2):
#     d = int(input("Enter the amount you want to deposit: "))
#     if (d > 0):
#        balance = balance + d
#        print("Balance after money deposited= ",balance)
#     else:
#         print("Invalid deposit amount")
# elif (c == 3):
#     w = int(input("Enter the  amount you want to withdraw: "))
#     if (w > 0):
#        if(w <= balance):
#           balance -= w
#           print("Balance after money withdrawl= ",w) 
#        else:
#           print("Insufficient balance")
#     else:
#         print("Invalid withdrawl amount")
# else:
#     print("Invalid input.\n Please choose 1 or 2 or 3.")  

# Q14. Write a program that categorizes a given age into different groups:
# Infant (0-1 year)
# Toddler (2-4 years)
# Child (5-12 years)
# Teenager (13-19 years)
# Adult (20-59 years)
# Senior (60 years and above)  
# a = int(input("Enter your age: "))
# if (0 <= a <= 1):
#     print("Infant")
# elif (2 <= a <= 4):
#     print("Toddler") 
# elif (5 <= a <= 12):
#     print("Child") 
# elif (13 <= a <= 19):
#     print("Teenager") 
# elif (20 <= a <= 59):
#     print("Adult") 
# elif (a >= 60):
#     print("Senior") 
# else:
#     print("Invalid input")                       

# Q15. Write a program that takes an integer (1-7) as input and prints the corresponding day of the week (1 for Monday, 2 for Tuesday, etc.).
i = int(input("Enter an integer between 1 to 7: "))
if (i == 1):
    print("Monday")
elif (i == 2):
    print("Tuesday")    
elif (i == 3):
    print("Wednesday")        
elif (i == 4):
    print("Thrusday")
elif (i == 5):
    print("Friday")
elif (i == 6):
    print("Saturday")    
elif (i == 7):
    print("Sunday")
else:
    print("Invalid input")                                