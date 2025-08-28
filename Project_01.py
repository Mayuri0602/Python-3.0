print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)") 
score = 0

question = input("What does CPU stand for? ")
if question.lower() == 'central processing unit':
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

question = input("What does HTML stand for? ")
if question.lower() == 'hyper text markup language':
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

question = input("What does CSS stand for? ")
if question.lower() == 'cascading style sheet':
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

question = input("What does RAM stand for? ")
if question.lower() == 'random access memory':
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

question = input("What does GUI stand for? ")
if question.lower() == 'graphical user interface':
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")                

print("Your got " + str(score) + " questions correct!" )
print("Your got " + str((score/5)* 100) + "%")