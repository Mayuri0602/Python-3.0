# 1. Write a program to print all natural numbers from 1 to n. – using while loop

i=1
n=500
while(n>=i):
    print(i)
    i+=1

# 2. Write a program to print all natural numbers in reverse (from n to 1). – using while loop

n=200
i=1
while(n>=i):
    print(n)
    n-=1

# 3. Write a program to print all alphabets from a to z. – using while loop

i=97
n=122
while(n>=i):
    print(chr(i))
    i+=1

# 4. Write a program to print all even numbers between 1 to 100. – using while loop

i=2
n=100
while(n>=i):
    print(i)
    i+=2

# 5. Write a program to find the sum of all odd numbers between 1 to n.

i=1
n=100
sum=0
while(n>=i):
     if(i%2!=0):
        sum+=i
     i+=1
print(sum)        


# 6. Write a program to count the number of digits in a number.

n=98978
count=0
while(n>0):
    r=n%10
    n=n//10
    count+=1
print(count) 

# 7. Write a program to calculate the sum of digits of a number.

n=1234
sum=0
while(n>0):
    r=n%10
    sum+=r
    n//=10
print(sum)

# 8. Write a program to find the first and last digit of a number. 

n=43876
last_digit=n%10
while(n>10):
    n=n//10
print("First digit= ",n, "last digit= ",last_digit)    

# 9. Write a program to find the sum of first and last digit of a number.

n=43873
last_digit=n%10
while(n>10):
    n=n//10
    sum=n+last_digit
print("Sum = ",sum)    

# 10. Write a program to enter a number and print its reverse.

n=int(input("Enter a number: "))
rev=0
while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10
print(rev)    

# 11. Write a program to find the power of a number using for loop.

for i in range(1,11):
    p=i**2
    print(p,end=" ")

# 12. Write a program to find all factors of a number.

n=12                     
for i in range(1,n+1):   #using for loop
    if(n%i==0):
      print(i,end=" ")


i=1
n=12
while(n>=i):            #using while loop
    if(n%i==0):
        print(i)
    i+=1    

# 13. Write a program to calculate the factorial of a number.

i=1
n=4
fact=1
while(n>=i):
    fact*=i
    i+=1
print(fact)    

# 14. Write a program to find LCM of two numbers.

a=8
b=12
if (a>b):
    greater=a
else:
    greater=b
while (True):
    if(greater%a==0) and (greater%b==0):
        print("LCM of", a, "and", b, "=",greater)
        break
    greater+=1        

# 15. Write a program to check whether a number is Prime number or not.

n=int(input("Enter a number: "))
i=2
count=0
while (n>i):
    if (n%i==0):
        count+=1
    i+=1
if( count==0) and (n>1):
        print("Number is prime")
else:
    print("Not a prime number")
      

n=int(input("Enter a number: "))
i = 2
while (i <= n):
    j = 2
    is_prime = True
    while j < i:
        if i % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        print(i,end=",")
    i += 1

# 16. Write a program to print all Prime numbers between 1 to n.

n=int(input("enter a number: "))
for i in range(2,n+1):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count+=1
            break   
    if(count==0):
      print(i,end=",")

# 17. Write a program to find all prime factors of a number.

num = int(input("Enter a number: "))
print(f"Prime factors of {num} are:")

i = 2
while i <= num:
    if num % i == 0:
        print(i, end=" ")
        num = num // i
    else:
        i += 1

# 18.Write a program to check whether a number is an Armstrong number or not.
# An Armstrong number is a n-digit number that is equal to the sum of the nth power of its digits. 
# For example – 6 = 61 = 6, 371 = 33 + 73 + 13 = 371

num = int(input("Enter a number: "))
orig = num
n = len(str(num))  # Count of digits
sum = 0

while (num > 0):
    digit = num % 10
    sum += digit ** n
    num //= 10

if orig == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# 19.Write a program to check whether a number is Strong number or not
# a. Strong number is a special number whose sum of factorial digits is equal to the original number.
# For example: 145 is a strong number. Since, 1! + 4! + 5! = 145

num=int(input("Enter a number: "))
orig=num
fact_sum=0
while(num>0):
    d=num%10
    fact=1
    for i in range(1,d+1):
        fact*=i
    fact_sum+=fact
    num//=10
if (orig==fact_sum):
    print("Strong number")
else:
    print("Not a strong number")    

# 20.Write a program to check whether a number is perfect number or not
# Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
# For example: 6 is the first perfect number
# Proper divisors of 6 are 1, 2, 3
# Sum of its proper divisors = 1 + 2 + 3 = 6.
# Hence 6 is a perfect number. 

num = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is NOT a Perfect Number")

# 21.Write a program to print fibonacci series upto n terms
# Fibonacci series is a series of numbers where the current number is the sum of the previous two terms. For Example: 0,1,1,2,3,8,13,21,...,(n-1th + n-2th)

n=13
a,b=0,1                  #using while loop
count=0
while(n>count):
     print(a,end=" ")
     a,b=b,a+b
     count+=1

a,b=0,1
print(a,b,end=" ")        #using for loop
for i in range(8):
     res=a+b
     print(res,end=" ")     
     a=b
     b=res     

# 22.Write a program to find ones complement of a binary number
#  One's complement of a binary number is defined as value obtained by inverting all binary bits. It is the result of swapping all
# 1s to 0s and all 0s to 1s.

binary = input("Enter a binary number: ")
ones_complement = ""

for bit in binary:
    if bit == '0':
        ones_complement += '1'
    elif bit == '1':
        ones_complement += '0'
    else:
        print("Invalid binary digit found!")
        break

print("One's complement:", ones_complement)  