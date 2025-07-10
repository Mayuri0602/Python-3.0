# list is a mutable and ordered datatype that stores values of same and different datatypes


# stopping value is not included
data = list(range(5,10))
print(data)

data2 = list(range(1,11,2))
print(data2)

data3 = list(range(10,1,-2))
print(data3)

data = [11,12,34,45,12,23,12]
data.sort()        # arrange in ascending order
print(data)
data.reverse()     # reverse the list
print(data)
print(data[::-1])  #reverse the list using reverse indexing and slicing
data.append(34)    # add element at the end of a list
print(data)        
data.remove(34)    # Removes only the first matching element and raises an error if the element is not found.
print(data)
# data.clear()       # clear all the elements from a list
# print(data)
data.extend([33,67])   # combines 2 list or add list in the end of an existing list
print(data)

# Removes and returns an item from the list.
# By default, it removes the last item if no index is given.
print(data.pop())
print(data)

data.insert(1,55)   #insert element 55 at index 1 
print(data)



"""tuples"""
data=(23,34,4,5,6,5,5,5) #it is immutable and ordered
# data[0]=90        # returns an error
# print(data)
print(data.index(34))
print(data.count(5))