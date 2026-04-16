import numpy as np
# # NumPy Practice Set — Session 4 & 5
# (Array Operations + Mathematical & Statistical Functions)
# EASY LEVEL
# 1. Create two arrays: a = [5, 10, 15] b = [1, 2, 3] Perform element-wise addition and multiplication.
# a=np.array([5,10,15])
# b=np.array([1,2,3])
# print("addition:",a+b)
# print("multiply",a*b)

# 2. Given array: arr = [4, 8, 12, 16] Extract elements greater than 10.
# arr=np.array([4,8,12,16])
# print("graterthan 10",arr[arr>10])

# 3. Create a 2×3 array of ones and add 5 to every element using broadcasting
# arr=np.ones((2,3))
# print(arr)
# print("add 5 using broadcasting:",arr+5)

# 4. Given array: arr = [10, 20, 30, 40] Compute:
# Mean
# arr=np.array([10,20,30,40])
# print("mean:",np.mean(arr))
# Sum
# print("sum",np.sum(arr))
# Maximum
# print("max",np.max(arr))

# 5. Convert 45 degrees into radians and compute its sine value.
# rad=np.deg2rad(45)
# sin_val=np.sin(rad)
# print("rad",rad)
# print("sin",sin_val)


# MEDIUM LEVEL
# 6. Create two arrays: a = [2, 4, 6, 8] b = [1, 2, 3, 4] Perform floor division and modulus operations.
# a=np.array([2,4,6,8])
# b=np.array([1,2,3,4])
# print("floor div",a//b)
# print("modulo",a%b)

# 7. Generate a 3×3 random integer matrix between 1 and 20. Find its standard deviation and variance.
# random_matrix=np.random.randint(1,20,(3,3))
# print(random_matrix)
# print("standard deviation:",np.std(random_matrix))
# print("variance:",np.var(random_matrix))

# 8. Create an array from 1 to 9 and reshape it into 3×3. Compute cumulative sum (cumsum).
# arr=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print(arr)
# print("cumulative sum (cumsum):",np.cumsum(arr))

# 9. Create array: arr = [-3, -1, 0, 1, 3] Apply:
# arr=np.array([-3,-1,0,1,3])
# # Square
# print("squre",np.square(arr))
# Square root (only valid values)
# print("squre root",np.sqrt(arr))

# ===========

# 10. Using logical operations: Given array: arr = [5, 10, 15, 20, 25] Extract values between 10 and 20 inclusive.
# arr=np.array([5,10,15,20,25])
# con1=arr>=10
# con2=arr<=20
# print("extract val",arr[np.logical_and(con1,con2)])


# HARD LEVEL

# 11. Create a 3×4 matrix using np.arange(). Add a 1D array [10, 20, 30, 40] using broadcasting.
# arr=np.arange(1,13).reshape(3,4)
# print(arr)
# arr2=np.array([10,20,30,40])
# print("add ad array using broad casting",arr+arr2)

# 12. Generate 1000 random numbers from normal distribution. Compute:
# arr=np.random.randn(1000)
# Mean
# print("mean:",np.mean(arr))
# Standard deviation
# print("Standard deviation",np.std(arr))
# 95th percentile
# print("95th percentiles",np.percentile(arr,95))

# 13. Create two matrices: A (2×3) and B (3×2). Transpose A and verify its shape.
# a=np.array([1,2,3,4,5,6]).reshape(2,3)
# print(a)
# b=np.array([9,8,7,6,5,4]).reshape(3,2)
# print(b)
# print("transpose a",a.T)

# 14. Create array: arr = [1, 2, 3, 4] Compute:
# arr=np.array([1,2,3,4])
# Exponential of each element
# print("Exponential:",np.exp(arr))
# Natural log
# print("natural log",np.log(arr))
# Log base 10
# print("base 10",np.log10(arr))

# 15. Create array: arr = [1.2, 2.5, 3.7, 4.1] Apply:
# arr=np.array([1.2,2.5,3.7,4.1])
# round()
# print("round:",np.round(arr))
# floor()
# print("floor",np.floor(arr))
# ceil() Explain differences based on output.
# print("ceil",np.ceil(arr))