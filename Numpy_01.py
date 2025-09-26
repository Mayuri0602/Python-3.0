import time

li1 = [1, 2, 3, 4]
li2 = [5, 6, 7, 8]
start = time.time()
for i in range(len(li1)):
    li1[i] += li2[i]
print(li1)                     # [6, 8, 10, 12]
print(f"Time taken for the operation: {time.time() - start}")


import numpy as np
import time

a1 = np.array([1, 2, 3, 4])
a2 = np.array([5, 6, 7, 8])
start = time.time()
a3 = a1 + a2
print(a3)                     # [6, 8, 10, 12]
print(f"Time taken for the operation: {time.time() - start}")


# numpy is homogenous datatype while list is heterogenous datatype
# numpy takes less memory as compared to list
# numpy takes less execution time while list take more time
# numpy has more functionality as compared to list


import numpy as np

arr = np.arange(1, 11)
print(arr)


arr = np.arange(1, 11).reshape(5,2)          # reshape (2,5) = should be factors of total elements
print(arr)

print(arr.ndim)      # n-dimensional array, i.e., 2 here 
print(arr.shape)     # (rows,cols)
print(arr.size)      # (rows * cols)
print(arr.itemsize)  # size of one element (in bytes)


new = np.array([[1,2], [3,4]], dtype = complex)
print(new)

c = np.array([1, 2, 3], dtype = float)
print(c)

a = np.zeros([3,4])
print(a)

a = np.ones([3,4])
print(a)

e = np.empty([2,4])    # uninitialized array
print(e)

arr = np.arange(1, 100, 3)
print(arr)

# linspace is used to generate evenly spaced numbers over a specified interval.
# np.linspace(start, stop, num=50, endpoint=True (means included ))
l = np.linspace(1, 20, 10, endpoint = False)
print(l)

l = np.linspace(1, 20, 10, endpoint = False).reshape(5, 2, 1)
print(l)

arr = np.arange(24).reshape(4,6)
arr1 = arr ** 2
print(arr1)

arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [2,3]])
print(arr1.dot(arr2))


a = np.random.default_rng()
b = a.random((2,3))
print(b)
print(b.sum(axis = 0))     # sum of each column, axis = 0
print(b.max(axis = 1))     # max of each row, axis = 1
print(b.min())
print(b.cumsum())


# Other Functions 

# arr = np.random.normal(mean, std_deviation, n)
# arr = np.random.rand(rows, cols)   :-   random no.s. generate in (uniform distribution)
# arr = np.fromfunction(f, (indices), dtype)
# arr = np.loadtxt('filename', dtype)


