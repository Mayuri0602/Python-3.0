# 1. Create a 1D NumPy array containing numbers from 5 to 50 with a step of 5.
import numpy as np
arr = np.arange(5,51,5)
print(arr)

# 2. Create a 2D array of shape (4, 3) filled with ones.
arr = np.ones((4,3))
print(arr)

# 3. Create an array of 6 equally spaced values between 0 and 1.
arr = np.linspace(0,1,6)
print(arr)

# 4. Create a 3×3 identity matrix.
arr = np.eye(3)
print(arr)

# 5. Find the shape, size, number of dimensions, and data type of a given array.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)
print(arr.size)
print(arr.ndim)

# 6. Convert the Python list [10, 20, 30, 40, 50] into a NumPy array.
li = [10, 20, 30, 40, 50]
print(np.array(li))

# 7. Reshape a 1D array of 16 elements into a 4×4 matrix.
arr = np.arange(1,17).reshape(4,4)
print(arr)

# 8. Flatten a 2D array into 1D using both flatten() and ravel(). Observe the difference.
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr.flatten())         # creates a copy of the original ones 
print(arr.ravel())           # creates a view of the original

# 9. Access the middle element of a 1D array.
arr = np.array([10, 20, 30, 40, 50])
mid = [len(arr)//2]
print(mid)

# 10. Reverse a NumPy array without using loops.
arr = np.array([10, 20, 30, 40, 50])
reversed = arr[::-1]
print(reversed)



# 1. Extract all even-indexed elements from a NumPy array.
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[::2])

# 2. Extract the last column from a 2D array.
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr[:,-1])

# 3. Slice a 1D array to get alternate elements starting from index 1.
arr = np.array([1, 22, 44, 3, 55])
print(arr[1::2])

# 4. Extract a 2×2 sub-matrix from a 3×3 matrix.
arr = np.random.rand(3,3)
print(arr)

sub = arr[0:2, 0:2]
print(sub)

# 5. Print all elements except the first and last element of an array.
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:-1])



# 1. Select all elements greater than 25 from a NumPy array.
arr = np.array([10, 25, 30, -5, 45, 50, -10, 60])
res = arr[arr > 25]
print(res)

# 2. Replace all negative values in an array with 0.
arr = np.array([10, 25, 30, -5, 45, 50, -10, 60])
arr[arr < 0] = 0
print(arr)

# 3. Extract only the elements divisible by 3.
arr = np.array([10, 21, 30, -5, 45, 50, -10, 60])
res = arr[arr % 3 == 0]
print(res)

# 4. Count how many elements are greater than the mean of the array.
arr = np.array([10, 21, 30, 5, 45, 50, -0, 60])
mean_val = arr.mean()
count = np.sum(arr > mean_val)
print("Mean: ", mean_val)
print("Count: ", count)


# 5. Find the indices of elements where the value is equal to 50.
arr = np.array([10, 21, 50, -5, 45, 50, -10, 60])
indices = np.where(arr == 50)
print(indices)


# 1. Add two NumPy arrays element-wise.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = a + b
print(result)


# 2. Perform matrix multiplication of two compatible matrices.
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

result = np.dot(A, B)
print(result)

rslt = A @ B
print(rslt)

# 3. Add a scalar value 10 to every element of a NumPy array.
arr = np.array([10, 20, 30])

result = arr + 10
print(result)

# 4. Add a 1D array of shape (3,) to a 2D array of shape (2, 3) using broadcasting.
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
arr1d = np.array([10, 20, 30])

result = arr2d + arr1d
print(result)
