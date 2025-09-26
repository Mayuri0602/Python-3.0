# 1. Create an Array
# Problem: Create a NumPy array from a list of space-separated integers.
# Input format: A list of integers separated by spaces.
# Example: 10 20 30 40 50
# Output format: The NumPy array.
# Example output: [10 20 30 40 50]
import numpy as np
li = [10, 20, 30, 40]
arr = np.array(li)
print(arr, type(arr))

# 2. Create an Array of Zeros
# Problem: Create an array of zeros with the specified shape.
# Input format: Two integers representing rows and columns.
# Example: 3 4
# Output format: A 3x4 array of zeros.
arr = np.zeros((3,4))
print(arr)

# 3. Create an Array of Zeros Like Another
# Problem: Given an array, create a zeros array with the same shape.
# Input format: A list of integers.
# Example: 5 6 7
# Output format: A zeros array with the same shape.
# Example output: [0 0 0]
l = [5, 6, 7]
arr = np.zeros_like(l)
print(arr)

# 4. Create an Array of Ones
# Problem: Create an array of ones with the specified shape.
# Input format: Two integers representing rows and columns.
# Example: 2 3
# Output format: A 2x3 array of ones.
arr = np.ones((2,3))
print(arr)

# 5. Create an Array of Ones Like Another
# Problem: Given an array, create an ones array with the same shape.
# Input format: A list of integers.
# Example: 9 8 7 6
# Output format: An array of ones with the same shape.
# Example output: [1 1 1 1]
arr1 = [5, 6, 7]
arr = np.ones_like(arr1)
print(arr)

# 6. Create an Uninitialized Array
# Problem: Create an uninitialized array with the given shape.
# Input format: Two integers representing rows and columns.
# Example: 2 2
# Output format: A 2x2 array with arbitrary uninitialized

# NumPy arrays created with np.empty() are uninitialized
arr = np.empty([2, 2])
print(arr)

# 7. Create an Array Like Another with Uninitialized Values
# Problem: Given an array, create an uninitialized array with the same shape.
# Input format: A list of integers.
# Example: 1 2 3 4 5
# Output format: An array with uninitialized values.
arr1 = [1, 2, 3, 4, 5]
arr2 = np.empty_like(arr1)
print(arr2)

# 8. Create an Array Using arange()
# Problem: Create an array using arange with start, end, and step values.
# Input format: Three integers separated by spaces.
# Example: 5 20 3
# Output format: A NumPy array with values starting from start to before end with step
# size.
# Example output: [5 8 11 14 17]
arr = np.arange(5, 20, 3)
print(arr)

# 9. Create a Linearly Spaced Array
# Problem: Use linspace to create n equally spaced numbers between start and end.
# Input format: Two floats and an integer: start, end, n.
# Example: 0 1 5
# Output format: An array with n equally spaced values.
# Example output: [0. 0.25 0.5 0.75 1. ]
arr = np.linspace(0, 1, 5, endpoint = 'True')
print(arr)

# 10. Generate Random Numbers (Uniform Distribution)
# Problem: Create an array of random numbers between 0 and 1.
# Input format: Two integers representing rows and columns.
# Example: 3 2
# Output format: A random array with uniform distribution.
arr = np.random.rand(3,2)
print(arr)

# 11. Generate Normally Distributed Random Numbers
# Problem: Create an array of normally distributed random numbers.
# Input format: Three values: mean, standard deviation, and number of elements.
# Example: 0 1 5
# Output format: A 1D array of n normally distributed values.
arr = np.random.normal(0, 1, 5)
print(arr)

# 12. Create an Array from a Function
# Problem: Create a 2D array where each element is the product of its row and column indices using fromfunction.
# Input format: Two integers representing rows and columns.
# Example: 3 3
# Output format: A 3x3 array where each element is i * j.
# Example output: [[0 0 0] [0 1 2] [0 2 4]]
def f(i, j):
    return i * j
arr = np.fromfunction(f, (3, 3), dtype=int)     # indices are 3,3 and rows = 0, 1, 2 & cols = 0, 1, 2
print(arr)

# 13. Load an Array from a File
# Problem: Load a 1D array from a file where numbers are space-separated.
# Input format: A file path (assume it's already present).
# Example file content: 1 2 3 4 5
# Output format: A 1D array with the numbers from the file.
# Example output: [1 2 3 4 5]
arr = np.loadtxt('numbers.txt', dtype=int)
print(arr, type(arr))