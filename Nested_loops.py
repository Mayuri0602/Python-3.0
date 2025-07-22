for i in range(1,6):
    for j in range(1,3):
        print(i,j)
    print("+++++")    


for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()    


for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


# Without nested loop
for i in range(5,0,-1):
    print("* " * i)


for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()        


for i in range(1,6):
    for j in range(6,0,-1):
        if j > i:   
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()    


for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            


for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or i==5 or i==j:                         
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()


for i in range(5,0,-1):
    for j in range(1,i+1):
        if j==1 or i==5 or i==j:      
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()


