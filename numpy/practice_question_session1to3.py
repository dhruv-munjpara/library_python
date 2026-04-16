import numpy as np 

# Section A — Easy Level Questions

# 1. Create a NumPy array using np.array() with elements [5, 10, 15, 20].

# arr1=np.arange(5,21,5)
# print(arr1)

# arr1=np.array([5,10,15,20])
# print(arr1)



# 2. Create an array from 0 to 18 with step size 3 using np.arange().
# arr2=np.arange(0,19,3)
# print(arr2)



# 3. Create 6 evenly spaced numbers between 1 and 3 using np.linspace().
# arr = np.linspace(1, 3, 6)
# print(arr)


# 4. Create a 2×4 zero matrix.
# zeromatrix=np.zeros((2,4))
# print(zeromatrix)


# 5. Create a 3×3 matrix filled with ones.
# onesmatrix=np.ones((3,3))
# print(onesmatrix)


# 6. Generate a 2×2 matrix of random numbers from uniform distribution.
# matrix = np.random.uniform(0, 1, (2, 2))
# print(matrix)


# 7. Create an identity matrix of size 4.
# print(np.identity(4))

# 8. Find the shape, size, and number of dimensions of the following array:
# array1=np.array([[1,2,3],[4,5,6]])
# print(array1.shape)
# print(array1.size)
# print(array1.ndim)
# ---

# # Section B — Medium Level Questions

# 9. Create an array from 1 to 12 and reshape it into a 3×4 matrix.
# arr1=np.arange(1,13)
# print(arr1)
# print(arr1.reshape(3,4))


# 10. Create a 4×4 matrix using np.arange() and transpose it.
# arr2=np.arange(1,17)
# print(arr2)
# arr3=arr2.reshape(4,4)
# print(arr3)
# print(arr3.T)
# print(np.transpose(arr3))


# 11. Generate 5 logarithmically spaced numbers between 10^1 and 10^3.
# print(np.logspace(1,3,5))




# 12. Create a random integer matrix of shape 3×3 with values between 10 and 50.
# arr4=np.random.randint(10,51,(3,3))
# print(arr4)


# 13. Create a 2×5 matrix using np.random.randn() and compute:
# array=np.random.randn(1,10).reshape(2,5)
# print(array)
#    - Total memory consumed (nbytes)
# print(array.nbytes)
#    - Size of one element (itemsize)
# print(array.itemsize)



# 14. Create an array of numbers from 1 to 9 and:
# arr = np.array([[1, 2], [3, 4]])
# print(arr)
        # 1. ravel()
        #     Returns a view of the original array (whenever possible).
        #     Changes in the raveled array reflect back to the original.
# r = arr.ravel()

#         2. flatten()
#                 Always returns a copy.
#                 Changes in the flattened array do NOT affect the original.
# f = arr.flatten()
# r[0] = 10
# f[1] = 20
# print("Original array:\n", arr)
# print("ravel output:", r)
# print("flatten output:", f)
# print(arr)
#    - Explain the difference
#Output explanation
# After r[0] = 100, the original array changes
# because ravel → view.
# After f[1] = 200, the original array does NOT change
# because flatten → copy.
# | Feature                  | `ravel()`            | `flatten()` |
# | ------------------------ | -------------------- | ----------- |
# | Returns                  | View (when possible) | Copy        |
# | Memory usage             | Low                  | Higher      |
# | Speed                    | Faster               | Slower      |
# | Changes affect original? | **Yes**              | **No**      |
# When to Use What?
# ✔ Use ravel() when you want better performance and you don’t mind if changes affect the original array.
# ✔ Use flatten() when you need a separate, independent array.



# 15. Create an empty 3×3 matrix and then fill it with 7 using broadcasting.
# arr=np.empty((3,3))
# print(arr)
#broadcasting
# arr[:]=7
# print(arr)

