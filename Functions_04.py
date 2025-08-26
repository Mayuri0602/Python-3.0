# High Order Function are the functions which take at least one function as parameter or returns a function as it results or performs both.

# map() function in Python is used to apply a specific function to each element of an iterable (like a list, tuple, or set)
# and returns a map object (which is an iterator).

s = ['1', '2', '3', '4']
res = map(int, s)           # map() applies int() to each element in s which changes their datatype from char to int.
print(list(res))


# By default, map() function returns a map object, which is an iterator.
# In many cases, we will need to convert this iterator to a list to work with the results directly.
n = [2,4,6,8,10]
def square(n):
    return n**2
res = list(map(square,n))
print(res)

# We can use a lambda function instead of a custom function with map() to make code shorter and easier.
a = [1, 2, 3, 4]
res = list(map(lambda x: x * 2, a))
print(res)

# map with multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))


# When to Use map()
# When we need to transform all elements in an iterable.
# When we prefer functional programming style over loops.
# When we want cleaner and shorter code.



# Filter() function is used to extract elements from an iterable (like a list, tuple or set) that satisfy a given condition.
# It works by applying a function to each element and keeping only those for which the function returns True.
# Syntax:- filter(function, iterable)

def even(n):
    return n % 2 == 0
a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)
print(list(b)) 


a = [1, 2, 3, 4, 5, 6, 8, 10]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))


a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
c = map(lambda x: x * 2, b)
print(list(c))


L = ["apple", "", None, "banana", 0, "cherry"]
A = filter(None, L)
print(list(A))


a = ["apple", "banana", "cherry", "kiwi", "grape"]
b = filter(lambda w: len(w) > 5, a)
print(list(b))



# "Generators" are special type of function that returns an iterator object.
# Use 'yield' instead of return to send back a single value to produce series of results over time.
# Lazy evaluation and memory-efficient
# When yield is executed, it pauses the function, returns the current value and retains the state of the function.
# This allows the function to continue from same point when called again, making it ideal for generating large or complex sequences efficiently.

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a      
        a, b = b, a + b

for num in fibonacci(10):
    print(num, end=" ")
