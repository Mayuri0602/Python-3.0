d = [34,54,56,6,65,7]
print(d[-3:-6:-1])
print(d[3:0:-1])

data = list(range(4,41,4))
print(data)

data=list(range(10)) 
print(data)             #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data=tuple(range(5,10))
print(data)
data=set(range(1,10,2))
print(data)

for i in range(1,11):
    print("2 x ",i ,"=", 2*i)

table = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{table} X {i} = {table*i}")    


data = 'welcome to regex'
for char in data:                # print(char): print particular character in different lines
    print(char, end='')          # welcome to regex 
    if char ==' ':               # welcome 
                                 # to 
                                 # regex
       print()



data2 = {'a':34, 'b':56, 'c':45} 
for i in data2:
    print(i)    ; 

fruits=['apple','orange','papaya','guava','litchi']
print(len(fruits))

for fruit in fruits:
    print(fruit)
