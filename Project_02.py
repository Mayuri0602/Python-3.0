import random

num = int(input("Enter a number: "))

if (num == 0):
    print("Please enter a number larger than 0 next time.")
    quit()

random_number = random.randint(0, num) 
guesses = 0

while True:
    guesses += 1
    user_guess = int(input("Make a guess: "))
    if (user_guess == random_number):
        print("You got it!")
        break
    elif (user_guess > random_number):
         print("You were above the number.")
    else:
        print("You were below the number.")

print("You got it in", guesses, "guesses.")             