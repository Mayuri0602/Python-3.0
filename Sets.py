# Sets are mutable and unordered datatype enclosed by curly brackets, each element in the set must be unique and immutable.
data = {23,45,67,90,11}
print(data)
data.add(66)
print(data)
data.clear()
print(data)

# empty set
empty_set = set()
print(type(empty_set))

d1 = {1,2,3,4}
d2 = {5,6,3,4}
print(len(d1))

print(d1.difference(d2))    # returns those elements from d1 which are not present in d2.
print(d2.difference(d1))
d2.difference_update(d1)    # used to modify a set by removing elements that are also present in one or more other specified sets or iterables. 
print(d2)

d1.discard(2)
print(d1)
d1.discard(40)            # Both discard and remove are used to remove an element from the set but the key difference is that 
print(d1)                 # discard does not raise any error whereas remove raises an error 
                          # when we remove the element which is not present in the set
# d2.remove(3)
# print(d2)
# d2.remove(40)
# print(d2)
  
d3 = {4,5,6,7,8}
d4 = {4,7,8,9,10}
d5 = {1,2,3,4,5}
n = d3.intersection(d4)
print(d3.intersection(d4))   # common elements from the set
n.intersection(d5)
print(n.intersection(d5))

d4.intersection_update(d3)
print(d4)

print(d3.isdisjoint(d4))     # returns True if there are no common elements present in the sets otherwise False

print(d3.issubset(d4))      # returns True if all the elements of set d3 are present in set d4

d5 = {1,2,3,4,5}
d6 = {2,3}
print(d5.issuperset(d6))     # returns True if set1,d5 contains all the elements of set2,d6 otherwise False

d5.pop()      # randomly removes an element from the set because it is unordered
print(d5)     # example:- lottery system

d7 = {11,22,33,44}
d8 = {44,55,66,77}

d7.symmetric_difference(d8)   # returns a new set by removing the common element
print(d7.symmetric_difference(d8))

print(d7.union(d8))    # returns all the elements in a new set removing the duplicate elements

d7.update(d8)    # all elements of d8 set are added in d7, that means d7 set is updated by d8
print(d7)

d7.update('ABC')    # single characters are updated in d7 as string 
print(d7)

d7.symmetric_difference(d8)        # returns a new set except common elements
print(d7.symmetric_difference(d8))


