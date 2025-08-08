for i in range(1,5):                  
    for j in range(i):
        print(" ",end=" ")      
    for k in range(1,5):
        print("*",end=" ")    
    print()       

# * * * * 
#   * * * *
#     * * * *
#       * * * *


r=5
c=7
for i in range(1,r):
    for j in range(1,c):
        if (i==1 or j==1 or i==4 or j==6):
            print("*",end="")
        else:
            print(" ",end="")    
    print()        

# ******
# *    *
# *    *
# ******


for i in range(1,6):
    for j in range(1,i+1):
        print(chr(65+j-1),end=" ")
    print()    

# A 
# A B
# A B C
# A B C D
# A B C D E


ch = 65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(ch),end=" ")
    ch+=1
    print()  
  
# A 
# B B
# C C C
# D D D D
# E E E E E


ch = 69
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(ch+j-1),end=" ")
    ch-=1
    print()    

# E 
# D E
# C D E
# B C D E
# A B C D E


for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")   
    print()        

#         1 
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5


rows=5
for i in range(1, rows+1):
    print("  " * (rows-i), end="")     
    for j in range(1, i+1):
        print("*", end=" ")
    print()

#         * 
#       * *
#     * * *
#   * * * *
# * * * * *


for i in range(1,6):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(1,7-i):
        print(k,end=" ")   
    print()     

# 1 2 3 4 5 
#   1 2 3 4
#     1 2 3
#       1 2
#         1


for i in range(1,6):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(1,7-i):
        print(chr(64+k),end=" ")     
    print()

# A B C D E 
#   A B C D
#     A B C
#       A B
#         A


for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end=" ")
    for k in range(1,6):
        print(k,end=" ")     
    print()

#         1 2 3 4 5 
#       1 2 3 4 5
#     1 2 3 4 5
#   1 2 3 4 5
# 1 2 3 4 5


for i in range(1,6):
    for j in range(1,6-i):
         print(" ",end=" ")
    for k in range(1,6):
         print(chr(64+k),end=" ")     
    print()

#         A B C D E 
#       A B C D E
#     A B C D E
#   A B C D E
# A B C D E


for i in range(1,5):
    for j in range(4-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()        

#       * 
#     * * *
#   * * * * *
# * * * * * * *


for i in range(1,5):
    for j in range(4-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print(chr(64+k),end=" ")
    print()   

#       A 
#     A B C
#   A B C D E
# A B C D E F G    


for i in range(1,5):
    for j in range(4-i):
        print(" ",end=" ")
    num=1    
    for k in range(1,2*i):
        print(num,end=" ")
        num+=1
    print()   

#       1 
#     1 2 3
#   1 2 3 4 5
# 1 2 3 4 5 6 7


rows = 5
for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(" ", end=" ")
    for k in range(1, 2*i):
        if k==1 or k==2*i-1 or i==rows:  
            print("*", end=" ")
        else:
            print(" ", end=" ")           
    print()

#         * 
#       *   *
#     *       *
#   *           *
# * * * * * * * * *



for i in range(5, 0, -1):         
    for j in range(5-i):            
        print(" ", end=" ")
    for k in range(2*i-1):             
        print("*", end=" ")
    print()

# * * * * * * * * * 
#   * * * * * * *
#     * * * * *
#       * * *
#         *



for i in range(1,5):
    for j in range(1, i + 1):
        print("*", end="")
    print()
for i in range(3, 0, -1):
    for k in range(1, i + 1):
        print("*", end="")
    print()

# *
# **
# ***
# ****
# ***
# **
# *



for i in range(1,5):
    for space in range(4 - i):   
        print(" ", end="")
    for j in range(i):              
        print("*", end="")
    print()
for i in range(3, 0, -1):
    for space in range(4 - i):   
        print(" ", end="")
    for k in range(i):              
        print("*", end="")
    print()

#    *                               
#   **                          
#  ***                               
# ****                          
#  ***              
#   **
#    *



rows=5
for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end="")
    for j in range(2*i - 1):
        print("*", end="")
    print()

for i in range(rows - 1, 0, -1):
    for space in range(rows - i):
        print(" ", end="")
    for k in range(2*i - 1):
        print("*", end="")
    print()

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *



for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()   

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5



for i in range(5, 0, -1):  
    for j in range(1, i + 1): 
        print(j, end=" ")
    print()

# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1



rows = 5
for i in range(1, rows + 1):
    for j in range(i, rows + 1):
        if i==1  or j==5 or i==j:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

# 1 2 3 4 5 
# 2     5
# 3   5
# 4 5
# 5


rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j==1  or j==i or i== 5:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

# 1 
# 1 2
# 1   3
# 1     4
# 1 2 3 4 5


rows = 9
cols = 15
row_gap = 1   
col_gap = 2

for i in range(rows):
    for j in range(cols):
        if (i==0 or i==rows-1 or j==0 or j==cols-1):
            print("*", end=" ")
        elif (i==row_gap+1 or i==rows-row_gap-2) and (col_gap+1 <= j <= cols-col_gap-2):
             print("*",end=" ")
        elif (j==col_gap+1 or j==cols-col_gap-2) and (row_gap+1 <= i <= rows-row_gap-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()                     

# * * * * * * * * * * * * * * * 
# *                           *
# *     * * * * * * * * *     *
# *     *               *     *
# *     *               *     *
# *     *               *     *
# *     * * * * * * * * *     *
# *                           *
# * * * * * * * * * * * * * * *    



rows = 5
for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(" ", end=" ")
    for k in range(1, 2*i):
        if k==1 or k==2*i-1:  
            print("*", end=" ")
        else:
            print(" ", end=" ")           
    print()    
for i in range(4,0,-1):
    for j in range(1,rows-i+1):
        print(" ",end=" ") 
    for k in range(1,2*i):
        if k==1 or k==2*i-1:
            print("*",end=" ")     
        else:
            print(" ",end=" ")      
    print()        

#         * 
#       *   *
#     *       *
#   *           *
# *               *
#   *           *
#     *       *
#       *   *
#         *