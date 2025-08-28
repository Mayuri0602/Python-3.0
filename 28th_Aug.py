# r = 5
# for i in range(1, r+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()    
# * 
# * * 
# * * *
# * * * *
# * * * * *


# r = 5
# for i in range(1, r+1):
#     for j in range(i-1):
#         print(" ",end=" ")
#     for k in range(r+1-i):
#         print("*",end=" ")        
#     print()
# * * * * *
#   * * * *
#     * * *
#       * *
#         *


# for i in range(1,6):
#     for j in range(6-i):
#         print("*",end=" ")
#     print()    
# * * * * * 
# * * * * 
# * * *
# * *
# *


# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()        
#         *
#       * *
#     * * *
#   * * * *
# * * * * *    


# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()        
#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()        
# * * * * * * * * * 
#   * * * * * * *
#     * * * * *
#       * * *
#         *    


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#         j+=1
#     print()    
# 1 
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5   
 

# for i in range(1,6):
#     for j in range(1,7-i):
#         print(j,end=" ")
#     print()    
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3
# 1 2
# 1    


# r = 4
# for i in range(1, r+1):
#     for space in range(r-i):
#         print(" ",end=" ")
#     for j in range(i, 2*i):
#         print(j,end=" ") 
#     for k in range(2*i-2, i-1, -1):
#         print(k,end=" ")  
#     print()    
#       1 
#     2 3 2 
#   3 4 5 4 3
# 4 5 6 7 6 5 4    



# for i in range(1,7):
#     for j in range(i):
#         print("*",end="")
#     print()    
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()    
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *    


# count=0
# for i in range(400,181,-1):
#       if i%3==0 and i%5==0:
#             count+=1
# print(count)            


# n = int(input("enter the number: "))
# sum=0
# while(n>0):
#       d=n%10
#       sum += d**2
#       n//=10
# print(sum)      


# s = "naman"
# m = len(s)//2
# print(s[0:m], s[m+1:])


# s = "ama"
# m = len(s)//2
# i= 0
# j = len(s)-1
# while (i<m):
#     if s[i] == s[j]:
#         print("True")
#     else:
#         print("False")    
#     i += 1
#     j -= 1


# for i in range(1,7):
#     for j in range(6-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()        
# for i in range(5,0,-1):
#     for j in range(6-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()     
#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *
# * * * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *    


# for i in range(1,5):
#     for j in range(4-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")    
#     print()    
# for i in range(3,0,-1):
#     for j in range(4-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()            
#       * 
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *    