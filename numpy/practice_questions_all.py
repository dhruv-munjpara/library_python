import numpy as np
# 1
# Create a 4×4 matrix using np.arange(1,17).
# Extract the second row.
# Extract the last column.
# Compute the mean of the entire matrix.
# arr=np.arange(1,17).reshape(4,4)
# print(arr)
# print("second row:",arr[1])
# print("last column:",arr[:,-1])
# print("mean",np.mean(arr))

# 2.
# Create array: arr = [5, 10, 15, 20, 25, 30]
# Extract elements greater than 10 AND less than 30.
# Find their cumulative sum.
# arr=np.array([5,10,15,20,25,30])
# con1=arr>10
# con2=arr<30
# print("Extract elements greater than 10 AND less than 30.",arr[np.logical_and(con1,con2)])
# print("cumulative sum",np.cumsum(arr))

# 3.
# Generate 10 random integers between 1 and 50.
# Sort them.
# Return indices that would sort the original array.
# Find the 75th percentile.
# np.random.seed()
# arr=np.random.randint(1,51,size=10)
# print(arr)
# print("sort",np.sort(arr))
# indices=np.argsort(arr)
# print("indices that sort array:",indices)
# print("75th percentile:",np.percentile(arr,75))

# 4.
# Create two 2×3 matrices.
# Concatenate them row-wise.
# Then split the result into 2 equal parts.
# arr=np.arange(1,7).reshape(2,3)
# arr1=np.arange(7,13).reshape(2,3)
# combained=np.concatenate((arr,arr1),axis=0)
# print("split",np.split(combained,2))

# 5.
# Create array: arr = [1, 2, 2, 3, 4, 4, 5]
# Remove duplicate values.
# Reverse the array using slicing.
# Compute standard deviation.
# arr=np.array([1,2,2,3,4,4,5])
# print("remove dublicate:",np.unique(arr))
# print("revers array",arr[::-1])
# print("starndard deviation",np.std(arr))

# 6.
# Create a 5×5 matrix using np.arange(1,26).
# Extract all elements greater than 10 and less than 20.
# Replace those values with 0 using boolean indexing.
# Compute total sum of modified matrix.
# array=np.arange(1,26).reshape(5,5)
# print(array)
# con1=array>10
# con2=array<20
# mask=np.logical_and(con1,con2)
# print("extract all element of grater than 10 and less than 20:",array[mask])
# array[mask]=0
# print("replace thos values with 0",array)
# print("total sum",array.sum())


# 7.
# Generate 1000 random numbers from normal distribution.
# Compute mean and standard deviation.
# Clip values between -1 and 1.
# Count how many values were clipped.
# arr=np.random.randn(1000)
# print("mean:",np.mean(arr))
# print("standard deviation",np.std(arr))
# clippied=np.clip(arr,-1,1)
# print("clip val",clippied)
# count_clip=np.sum(clippied)
# print("count clip val",count_clip)


# 8.
# Create array: arr = [10, 20, np.nan, 40, 50, np.nan]
# Compute mean ignoring NaN.
# Replace NaN values with 0.
# Compute new mean.
# arr=np.array([10,20,np.nan,40,50,np.nan])
# print(arr)
# print("ingnpring nan mean:",np.nanmean(arr))
# arr_no_nan=np.nan_to_num(arr,nan=0)
# print("replace nan with 0:",arr_no_nan)
# print("compute new mean",arr_no_nan.mean())

# 9.
# Create two matrices: A (3×3) using np.arange() B (3×3) random integers between 1 and 10.
# Perform element-wise multiplication.
# Compute 90th percentile of result.
# Transpose the result.
# a=np.arange(0,9).reshape(3,3)
# b=np.random.randint(1,10,(3,3))
# print(a)
# print(b)
# c=a*b
# print("ele wise mul:",c)
# print("90 th percentile",np.percentile(c,90))
# T=c.T
# print("transpose result",T)


# 10.
# Create array: arr = np.arange(1,21)
# Reshape into 4×5 matrix.
# Extract elements divisible by both 2 and 3.
# Insert value 999 at index 2.
# Delete last element.
# Verify whether all remaining values are positive.
# arr=np.arange(1,21)
# reshaped=arr.reshape(4,5)
# print(reshaped)
# divide=(reshaped%2==0)&(reshaped%3==0)
# print("element diveded by 2 and 3",reshaped[divide])
# arr2=np.insert(arr,2,999)
# print(" Insert value 999 at index 2:",arr2)
# arr3=np.delete(arr2,-1)
# print("Delete last element:",arr3)
# check_positive = np.all(arr3 > 0)
# print("\nAre all values positive:", check_positive)



