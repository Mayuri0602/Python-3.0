# Write a function to check if a number is prime or not.

def check_prime(a):
    # if a <= 1:
    #     return False
    # if a == 2:
    #     return True
    # if a%2 == 0:
    #     return False
    i=2
    count=0
    while (a>i):
      if (a%i==0):
        count+=1
      i+=1
    if(count==0) and a>1:
      print("Prime number")
    else:
      print("not")

check_prime(3)           


# Print the pattern. 

def star(n):
    num=1
    ch=65
    for i in range(1,n+1):
        for j in range(n+1):
           if i%2 != 0:
             print(num,end="")
             num+=1
           else:
             print(chr(ch),end="")
             ch+=1
        print()     
star(4)        



s="saras"
i=0
j=len(s)
while (i < j):
    print(i,s[i])
    i+=1 


# Check if the given string is pallindrome or not.

s = "saras"
i = 0
j = len(s) - 1
while i < j:
    if s[i] != s[j]:
        print("Not Palindrome")
        break
    i += 1
    j -= 1
else:
    print("Palindrome")


# Print the longest name from the list.

names= ["yash","saini","preeti"]
longest=names[0]
for name in names:
    if len(name) > len(longest):
       longest=name
print(name)     


# Print the longest pallindrome name from the given string:
data = "user aman ama TRASART regex"
new_data = data.split()          # string to list
longest=" "

for word in new_data:
   s=word.lower()
   i,j = 0, len(s)-1
   is_pal = True

   while i < j:
      if s[i] != s[j]:
         is_pal = False
         break         
      i +=1
      j -=1
   
   if is_pal and len(word)>len(longest):
      longest=word

print(longest)      


