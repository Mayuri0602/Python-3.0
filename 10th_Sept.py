# Coke Machine question

# a = 50

while (a > 0):
      print("Amount due = ", a)
      c = int(input("Insert a coin(5, 10, 25): "))

      if c in [5, 10, 25]:
            a -= c
      else:
            print("Invalid input")
      c = a
      print("Amount due: ", c)



# Camel Case Question

s = input("Camel case: ")
new_s = " "

for i in s:
    if i.isupper():
        new_s += "_" + i.lower()
    else:
        new_s += i

print(new_s)   


# Twitter Question

s = input("Enter a name: ")
for i in s:
    if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print("", end="")
    else:
        print(i, end="")


# Vanity Plate Question

s = input("Plate: ")

if 2 <= len(s) <= 6 and s[:2].isalpha():
    
    for i, c in enumerate(s):
        if c.isdigit():
            if c == "0" and (i == 2):   
                print("Invalid")
                break
            if not s[i:].isdigit():
                print("Invalid")
                break
    else:
        print("Valid")
else:
    print("Invalid")


# Nutrition Facts Question









          