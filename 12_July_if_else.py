# 9.  Number Sign and Parity
       #  Check if a number is:
       #  Positive even
       #  Positive odd
       #  Negative even
       #  Negative odd
       #  Zero
n = int(input("Enter a number: "))
if (n > 0) and (n % 2 == 0):
    print(f"{n} is positive and even")
elif (n > 0) and (n % 2 != 0):
    print(f"{n} is positive and odd")
elif (n < 0) and (n % 2 == 0):
    print(f"{n} is negative and odd")  
elif (n < 0) and (n % 2 != 0):
    print(f"{n} is negative and odd")
elif (n == 0):
    print("Zero")
else:
    print("Invalid input")                  


# 12. Input three sides and determine if triangle is:
# Equilateral
# Isosceles
# Scalene
# Check if three sides can form a valid triangle using triangle inequality.
s1 = float(input("Enter the first side of a triangle: "))
s2 = float(input("Enter the second side of a triangle: "))
s3 = float(input("Enter the third side of a triangle: "))

if (s1 + s2 > s3) and (s2 +s3 > s1) and (s1 + s3 > s2):
    if (s1 == s2 == s3):
        print("Equilateral triangle")
    elif (s1 == s2 or s2 == s3 or s3 ==s1):
        print("Isosceles triangle")
    else: 
        print("Scalene triangle")
else: 
    print("Not a triangle")
                    

# 14. Take input as `red`, `yellow`, or `green` and print corresponding message (Stop/Slow/Go).
c = input("Enter the traffic signal colours(red, yellow, green): ")
if (c == 'red'):
    print("Stop")
elif (c == 'yellow'):
    print("Slow")
elif (c == 'green'):
    print("Go")        
else:
    print("Invalid input")  
  

# 16. Check if a number is in the range 1–100.
n = int(input("Enter the number: "))
if (n > 0 and n < 101):
    print("Number is in the range")
else:
    print("Number is not in the range")    


# 17. If balance is sufficient, deduct amount. Else print "Insufficient Balance".
balance = 2000
amt = int(input("Enter the amount: "))
if (balance > amt):
    balance -= amt
    print("Amount deducted = ",balance) 
else:
    print("Insufficient balance")


# 18. Input temperature in °C and classify:
# Cold (<10)
# Moderate (10–25)
# Hot (>25)
t = float(input("Enter the temperature(in Celsius degree): "))
if (t < 10):
    print("Cold")
elif (t >=10 and t <= 25):
    print("Moderate")
elif (t > 25):
    print("Hot")        
else:
    print("Invalid input")


# 19. Check if password length is:
# Weak (<6)
# Moderate (6–10)
# Strong (>10)
p = input("Enter the password: ")
length = len(p)
if (length < 6):
    print("Weak password")
elif (length >= 6 and length <= 10):
    print("Moderate password")
elif (length > 10):
    print("Strong password")
            

# 21. Input username and password:
# If both correct → "Welcome"
# Username correct, password wrong → "Incorrect Password"
# Username wrong → "User not found"
username = 'pooja'
password = 'puja123'
u = input("Enter the username: ")
p = input("Enter the password: ")
if  (u == username and p == password):
    print("Welcome")
elif (u == username and p != password):
    print("Incorrect password")
elif (u != username):
    print("Username not found")
else:
    print("Error !\n Try again.")            


# 22. Electricity Bill Calculator
# Units consumed:
# First 100 units: ₹1/unit
# Next 100 units: ₹1.5/unit
# Beyond 200: ₹2/unit
# Calculate total bill.
print("Electricity bill details:")
units = float(input("Enter the number of units consumed = "))
bill_amt = 0
if units <= 100:
    bill_amt = units * 1
elif units <=200:
    bill_amt = (100 * 1) + (units - 100) * 1.5
elif units > 200:
    bill_amt = (100 * 1) + (100 * 1.5) + (units - 200) * 2
print(f"{bill_amt}rupees for the {units} consumed")
    

# 23. Time of Day Message
# Input time (0–23). Print:
# Morning (5–11)
# Afternoon (12–17)
# Evening (18–21)
# Night (22–4)
time = int(input("Enter the time(0-23): "))
if time >= 5 and time <= 11:
    print("Good Morning")
elif time >=12 and time <= 17:
    print("Good Afternoon")
elif time >=18 and time <=21:
    print("Good Evening")
elif time >=22 and time <= 4:
    print("Good Night")    
else:
    print("Invalid input")   


# 24. Day Type Checker
# Input day name and Print:
# "Weekend" for Saturday/Sunday
# "Weekday" otherwise
day = input("Enter the name of the day: ").lower()
if day == 'saturday' or day == 'sunday':
    print("Weekend")
elif day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday':
    print("Weekday")    
else:
    print("Invalid input")

# # or

weekends = {'saturday', 'sunday'}
weekdays = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
day = input("Enter the name of the day: ").lower()
if day in weekends:
    print("Weekend")
elif day in weekdays:
    print("Weekday")
else:
    print("Invalid input")


# 26. Input age and nationality. Must be:
# Indian
# Age ≥ 18
# Then eligible to vote
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
if age >= 18 and nationality == 'Indian':
    print("Eligible to vote")
else:
    print("Not eligible to vote")    


#  27. Give user 3 attempts to enter correct password.
# If fails 3 times, print "Account Locked".           
password = input("Enter the password: ")
check = input("Enter the login password: ")
if password == check:
    print("Success")
else:
    check = input("Enter the login password again: ")   
    if password == check:
        print("Success")
    else:
       check = input("Enter the login password for the last time: ") 
       if password == check:
           print("Success")
       else:
           print("Account locked")    


# 28. A student is eligible for a scholarship if:
# GPA is above 3.5
# If income is less than ₹200,000, print "Full Scholarship"
# If income is between ₹200,000 and ₹500,000, print "Half Scholarship"
# Else, print "Merit-Based Scholarship Only"
# If GPA is between 3.0 and 3.5, print "Partial Scholarship"
# If GPA is below 3.0, print "Not eligible"

gpa = float(input("Enter the gpa score: "))
if gpa < 3.0:
    print("Not eligible")
elif gpa >= 3.0 and gpa <= 3.5:
    print("Partial Scholarship")
elif gpa > 3.5:
    income = int(input("Enter the income: "))
    if income < 200000:
        print("Full Scholarship")
    elif income >= 200000 and income < 500000:
        print("Half Scholarship")
    else:
        print("Merit - Based Scholarship")        

