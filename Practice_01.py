# Q.1 Reverse a list without using built-in methods.
# Input: [10, 20, 30, 40]
# Output: [40, 30, 20, 10]
data = [10, 20, 30, 40]
rev_data = []
for i in data:
    rev_data = [i] + rev_data
print(rev_data)    


# Q.2 Create a user defiend list and calculate sum of all elements that present in list . 
# data = list(map(int,input("enter the numbers : ").split()))
# print("data = ",data)
# sum = 0
# for i in data:
#     sum += i
# print(sum)    


# Q.3 Remove all duplicates from a list while maintaining order.
# Input: [1, 2, 2, 3, 4, 3]
# Output: [1, 2, 3, 4]
data = [1, 2, 2, 3, 4, 3]
new_data = []
for i in data:
    if i not in new_data:
        new_data.append(i)
print(new_data)        


# Q.4 Find the second largest number in a list.
# Input: [12, 35, 1, 10, 34, 1]
# Output: 34
data = [12, 35, 1, 10, 34, 1]
new_data = list(set(data))
new_data.sort()
print(new_data[-2])


# Q.5 Convert a list of tuples into a dictionary.
# Input: [("a", 1), ("b", 2), ("c", 3)]
# Output: {'a': 1, 'b': 2, 'c': 3}
data = [("a", 1), ("b", 2), ("c", 3)]
dict = {}
for key,value in data:
    dict[key] = value
print(dict)    


# Q.6 Write a function that takes a tuple of integers and returns a tuple with only even numbers.
# Input: (1, 2, 3, 4, 5, 6)
# Output: (2, 4, 6)
data = (1, 2, 3, 4, 5, 6)
new_data = tuple(x for x in data if x%2 == 0)
print(new_data)      


# Q.7 Find common elements between two tuples.
# Input: (1, 2, 3), (2, 3, 4)
# Output: (2, 3)
t1 = (1, 2, 3)
t2 = (2, 3, 4)
common = tuple(set(t1) & set(t2))
print(common)


# Q.8 Merge two dictionaries and sum values of common keys.
# Input: {'a': 10, 'b': 20}, {'a': 5, 'c': 7}
# Output: {'a': 15, 'b': 20, 'c': 7}
d1 = {'a': 10, 'b': 20}
d2 = {'a': 5, 'c': 7}
copy = d1.copy()
for key,value in d2.items():
    if key in copy:
       copy[key] += value
    else:
       copy[key] = value
print(copy)       
