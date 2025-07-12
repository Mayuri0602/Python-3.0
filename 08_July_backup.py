# Shorthand Operators
# +=
# -=
# *=
# /=


# Bitwise Operators:-
# | -> or
# & -> and
# ^ -> XOR
# ~ -> not
# >> -> right shift
# << -> left shift

a = 35
print(bin(a))

# 2^5  2^4  2^3  2^2  2^2  2^0

# 0r
a = 21
b = 17
print(bin(a))
print(bin(b))
print(a|b)

# and
c = 23
d = 13
print(bin(c))
print(bin(d))
print(c&d)

# not :- add 1 to the number and then change the sign
print(~7)

# xor :- same digits=0 and different digits=1,  e.g. 11=0, 00=0, 10=1, 01=1
print(21^35)

# left shift
print(12<<1)  
# means shift 1 bit to the left side

print(12>>2)
# shift 2 bits to the right side
 

# Associativity :- we do calculation from the right side
print(2**2**3) 
# 2**3 = 8 and then 2**8 = 256


# Operator Precedence:-

# () parentheses
# ** exponential
# * multiplication
# / divide
# + addition
# - subtraction

# xor bitwise operator
print(10^15)

# left & right shift
print(12<<1)
print(12>>1)

print(13>>1)
print(13<<1)
