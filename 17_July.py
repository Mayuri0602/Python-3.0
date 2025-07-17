Print even numbers from 1 to 20 using while loop with step value of 3 . 
i=1
n=20
while(i<=n):
    if(i%2==0):
        print(i)
    i+=3    


# Calculate the sum of the first n natural numbers using a while loop
# Input: n
# Output: sum
i=1
sum=0
n=int(input("Enter a number:"))
while(i<=n):
    sum+=i
    i+=1
print(sum)    


#  Print multiplication table of a number using while loop
# Input: number n
# Output: n × 1 to n × 10
i=1
n=int(input("Enter a number:"))
while(i<=10):
    print(f"{n} x {i} = {n*i}")
    i+=1


# Reverse a number using while loop
# Input: number 1234
# Output: 4321
n=1234
rev=0
while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10
print(rev)    


# Count the number of digits in a number using while loop
# Input: 45678
# Output: 5
n=1234
count=0
while(n>0):
    n=n//10
    count+=1
print(count)    


# Calculate factorial of a number using while loop
# Input: n
# Output: n!
i=1
n=5
fact=1
while(i<=n):
    fact*=i
    i+=1
print(fact)    

# Write a program to print sum of digits of a number using while loop
sum=0
n=43332
while(n>0):
    sum=sum+(n%10)
    n=n//10
    i+=1
print(sum)    


# Armstrong number
n=int(input("Enter a number:"))
orig=n
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if(orig==sum):
    print("Armstrong number")
else:
    print("Not an armstrong number")        


# Pallindrome  number 
n=int(input("Enter a number:"))
rev=0
orig=n
while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10
print("reversible of a number:",rev )
if (orig==rev):
    print("Pallindrome number")
else:
    print("Not a pallindrome number")   


# Print numbers from 90 to 20
n=90
while(n>=20):
    print(n)
    n-=1      
   
