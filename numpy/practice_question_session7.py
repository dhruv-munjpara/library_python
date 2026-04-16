import numpy as np
# 1.Create an array from 1 to 15.
# Split it into 5 equal parts.
# arr=np.arange(1,16)
# print(np.split(arr,5))

# Q2.
# Create an array from 1 to 11.
# Split it into 4 parts using array_split() .
# arr=np.arange(1,12)
# print(np.array_split(arr,4))

# Q3.
# Given: arr = np.array([10, 20, 30, 40, 50])
# Insert 25 at index 2
# arr = np.array([10, 20, 30, 40, 50])
# print(np.insert(arr,2,25))


# Q4.
# Given: arr = np.array([[1,2], [3,4]])
# Insert a new row [5,6] at index 1
# arr = np.array([[1,2], [3,4]])
# print(np.insert(arr,1,[5,6],axis=0))

# Q5.
# Given: arr = np.array([5, 10, 15])
# Append 20 and 25 at the end.
# arr=np.array([5,10,15])
# print(np.append(arr,[20,25]))

# Q6.
# Given: arr = np.array([[1,2], [3,4]])
# Append column [7,8] to this array.
# arr=np.array([[1,2],[3,4]])
# print(np.append(arr,[[7],[8]],axis=1))

# Q7.
# Given: arr = np.array([100, 200, 300, 400, 500])
# Delete: a) Element at index 3
# b) First two elements
# arr = np.array([100, 200, 300, 400, 500])
# print(np.delete(arr,3))
# print(np.delete(arr,[0,1]))

# Q8.
# Given: arr = np.array([[1,2], [3,4], [5,6]])
# Delete the second row.
# arr = np.array([[1,2], [3,4], [5,6]])
# print(np.delete(arr,1,axis=0))


# Q9.
# Create: arr = np.array([1,2,3,4])
# Create:
# view_arr using view()
# copy_arr using copy()
# Modify arr[0] = 999
# Print all three arrays. Explain what happened
# arr = np.array([1,2,3,4])
# view_arr=arr.view()
# copy_arr=arr.copy()
# arr[0]=999
# print(arr)
# print(view_arr)
# print(copy_arr)

# Q10.
# Create array from 1 to 6. Reshape it into 2×3 matrix. Change element at position (0,1) to 100.
# arr=np.array([1,2,3,4,5,6]).reshape(2,3)
# arr[0,1]=100
# print(arr)

# Q11.
# Given: arr = np.array([[1,2,3], [4,5,6]])
# Apply:flatten()
# ravel()
# Modify first element of both results. Observe difference.
# arr11 = np.array([[1,2,3],
#                   [4,5,6]])
# flat = arr11.flatten()
# rav = arr11.ravel()
# flat[0] = 999
# rav[1] = 888
# print("Original:\n", arr11)
# print("Flatten:", flat)
# print("Ravel:", rav)

# Q12.
# Create array from 1 to 12. Split into 3 equal parts. Delete last element from each part. Combine all remaining
# elements into a single array
arr12 = np.arange(1,13)
parts = np.split(arr12, 3)
print(parts)
modified_parts = [np.delete(p, -1) for p in parts]
print(modified_parts)
result = np.concatenate(modified_parts)
print(result)
