'''
Write a program to take input in following intro

my name is ----
i am --- year old
i studying ----- course

'''
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter the course name: ")

print(f"\nMy name is {name}.")
print(f"I am {age} years old.")
print(f"I am studying {course} course.")