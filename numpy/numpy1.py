import numpy as np
# matrix=np.array([[1,2,3],[4,5,6]])

# print("2D Array")
# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)
# print(matrix.size)
# print(matrix.dtype)
# print(matrix.itemsize)
# print(matrix.nbytes)


# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# print("addition",arr1+arr2)
# print("subrtaraction",arr1-arr2)
# print("multiplication",arr1*arr2)
# print("Division",arr1/arr2)


# numbers=np.arange(1,21)
# print(numbers)

# matrix2=np.arange(1,10).reshape(3,3)
# print(matrix2)

# array1=np.array([2,4,6])
# print(array1*10)


# array2=np.zeros((4,5))
# print(array2.shape)
# print(array2.ndim)

# array3=np.linspace(0,1,5)
# print(array3)

# arrray4=np.logspace(1,3,4)
# print(arrray4)


# np.random.seed(42)
# print("umiform:",np.random.rand(2,2))
# print("nominal:",np.random.randn(2,2))
# print("random integer:",np.random.randint(1,10,(2,3)))
# print("random choice:",np.random.choice([10,20,30],size=9))


# arr=np.arange(1,10)
# print(arr)

# reshaped=arr.reshape(3,3)
# print("reshape:\n",reshaped)
# print(arr)

# print("ravel:",reshaped.ravel())
# print(arr)

# print("flatten",reshaped.flatten())
# print(arr)

# arr.resize(3,3)
# print("resize:\n",arr)

# print(arr)

# array1=np.array([1,2,3,4,5,6]).reshape(2,3)
# print(array1)
# array2=np.array([7,8,9]).reshape(1,3)
# print(array2)
# print(array1+array2)


# aa=np.empty((4,3))
# print(aa)
# aa[:]=5.5
# print(aa)

# aa=np.array([1,2,3,4,5,6,7,8]).reshape(2,4)
# bb=np.array([9,8,7,6,5,4,3,2,1,12,13,14]).reshape(3,4)
# print(aa)
# print(bb)
# print(bb+aa)


# arr=np.arange(1,11)
# print(arr)
# print(arr[1])
# print(arr[2])
# print(arr[3])
# print(arr[4])
# print(arr[5])
# print(arr[6])
# print(arr[7])
# print(arr[8])
# print(arr[9])
# print("nagative")
# print(arr[-1])
# print(arr[-2])
# print(arr[-3])
# print(arr[-4])
# print(arr[-5])
# print(arr[-6])
# print(arr[-7])
# print(arr[-8])
# print(arr[-9])


# a=np.array([1,2,3,4]).reshape(2,2)
# print(a)
# a1=np.array([1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3]).reshape(4,4)
# print(a1)
# print(a1[2,0])
# print(a1[3,3])
# print(a1[1,2])
# print(a1[0,0])
# print(a1[3,1])




# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).reshape(4,4)
# print(a)
# print(a[0,0])
# print(a[0,1])
# print(a[0,2])
# print(a[0,3])
# print(a[1,0])
# print(a[1,1])
# print(a[1,2])
# print(a[1,3])
# print(a[2,0])
# print(a[2,1])
# print(a[2,2])
# print(a[2,3])
# print(a[3,0])
# print(a[3,1])
# print(a[3,2])
# print(a[3,3])



# arr=np.array([1,3,7,9,40,60,100])
# print(np.percentile(arr,90))
# print(np.percentile(arr,80))



# array=np.array([1,2,3,4,5])
# print("gtarer than",array>4)
# print("gtarer than",array[array>4])

# array=np.array([1,2,3,4,5])
# print(np.where(array>3))#index
# print(array[np.where(array>3)])#values


# 1
# array=np.array([10,20,30,40,50])
# # first element
# print("first ele",array[0])
# print("last ele:",array[-1])

# 2
# array=np.array([5,10,15,20,25,30])
# print("extract ele from 1 to 4 using sliceing",array[0:4])
# 3
# arr=np.array([0,2,4,6,8,10])
# print("exteract all second ele",arr[0:-1:2])

# 4
# arr=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print("print ele located at row 2 or column 1 ",arr[1,0])

# 5
# arr=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print("first  row",arr[0])
# print("second row",arr[1])

# 6
# arr=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# first=arr[0]
# second=arr[1]
# print(first)
# print(second)
# print("[2,3] sub matrix:",first[1:])
# print("[5,6]sub matrix:",second[1:])
# # or
# print(arr)
# print(arr[0:2,1:3])
# print(arr[1:3,0:2])

# arr=np.array([10,20,30,40,50])
# print(arr[[0,2,4]])

# 8
# arr=np.array([5,10,15,20,25,30])
# print("using boolean indexing extract ele grater than 12",arr>12)

# 9
# arr=np.array([3,6,9,12,15])
# print("use np.where() to find indices where values are grater than 8",np.where(arr>8))

# 10
# arr=np.array([1,2,3,4,5])
# print("revers the array using sliceing :",arr[::-1])

# 11
# a=np.array([2,4,6])
# b=np.array([1,2,3])
# print("ele wise multiplication",a*b)
# print("power of a",a**2)

# 12
# arr=np.array([4,9,16,25])
# print("squre root",np.sqrt(arr))
# print("mean",np.mean(arr))
# print("maximun values",np.max(arr))



# session 7
# 1
# arr=np.arange(1,16)
# print("split it into equal parts",np.split(arr,5))


# 2
# arr=np.arange(1,12)
# print("split into 4 parts",np.array_split(arr,4))

# 3
# arr=np.array([10,20,30,40,50])
# print(np.insert(arr,2,25))

# 4
# arr=np.array([[1,2],[3,4]])
# print(np.insert(arr,1,[5,6],axis=0))

# 5
# arr=np.array([5,10,15])
# print(np.append(arr,[20,25]))


# 6
# arr=np.array([[1,2],[3,4]])
# print(np.append(arr,[7,8))
# ================================


# 7
# arr=np.array([100,200,300,400,500])
# print("delete ele at index 3",np.delete(arr,3))
# print("delete first two",np.delete(arr,[0,1]))

# 8
# arr=np.array([[1,2],[3,4],[5,6]])
# print("delete second row",np.delete(arr,1,axis=0))

# 9
# arr=np.array([1,2,3,4])
# print("original array",arr)
# arr[0]=999
# print("modify arr",arr)
# Why this happens?
# Because NumPy arrays are:
# mutable
# stored in continuous memory
# So when you assign arr[0] = 999,
# NumPy directly updates that exact position in memory.



# 10
# arr=np.arange(1,7).reshape(2,3)
# print(arr)
# arr[0,1]=100
# print(arr)

# 11
# arr=np.array([[1,2,3],[4,5,6]])
# # flatten
# f=arr.flatten()
# f[0]=999
# # ravel
# r=arr.ravel()
# r[0]=888
# print("original array after modify:\n",arr)
# print("flatten () result :\n",f)
# print("arvel () rsult:\n",r)
# diffrence
# flatten() is return copy not changes in original 
# ravel() is return viwe its changes in original


# 12
# arr=np.arange(1,13)
# print(arr)
# parts=np.split(arr,3)
# print(parts)
# modify=[p[:-1] for p in parts]
# print(modify)
# final_arr=np.concatenate(modify)
# print(final_arr)


# session -8
# unique
# arr=np.array([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,])
# print(np.unique(arr))

# sort
# arr=np.array([4,5,7,3,8,6,2,9,1])
# print(np.sort(arr))

# argsort
# arr=np.array([30,10,50,20])
# print(np.argsort(arr))


# np.nonzero()
# arr=np.array([1,0,2,0,3])
# print(arr)
# print(np.nonzero(arr))

