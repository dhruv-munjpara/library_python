import numpy as np
# import the numpy 

# matrix1=np.array([1,2,3,4])
# print(matrix1)
# parameter is list [1,2,3,4] we will anything write in the list so it is give array

# arr=np.array([1,2,3,4,5])
# print(type(arr))
# this is the given the type of the array 


# if in the list we will create a loop and the iterator all element then add
# array1=np.array([1,2,3,4,5,6])
# print("add all elememt to 5",array1+5)
# but inthis case we will print array+5 so all element add 5 turn by turn


# vectorization:so in this numpy we will appying an operation to all elememnt with out loop


# matrix2=np.array([[1,2,3,4],
#                 [5,6,7,8]])
# print(matrix2)
# so paramenter is the ([[1,2,3,4],[5,6,7,8]]) so it is the list and its a 2d matrix
# print(matrix2.shape)
# so array_name.shape is the paramenter and is this give shape of the matrix like our matrix is ([[1,2,3,4],[5,6,7,8]]) so its shape is 2 rows and 4 column


# # we will discuss the array properties
# array1=np.array([1,2,3,4])
# print("this is the array",array1)
# print("this is the shape of the array",array1.shape)
# print("this is the demention of the array",array1.ndim)
# print("this is the size of the array",array1.size)
# print("this is the data type of the array",array1.dtype)

# Explanation:
# shape → (rows, columns)
# ndim → number of dimensions->1 demention
# size → total elements in array->how many elemnt are there in the array its the givr size of the array
# dtype → data type of elements->ite give the type of the data


# array of zeros
# zeros_array=np.zeros((2,3))
# print(zeros_array)
# in this case it will give to 2 rows and 3 column with o array like [[0. 0. 0.] [0. 0. 0.]] 
# method=np.zero(shape)
# parameter=(row,column)/shape
# application=    1) Initialize array for calculations
                #   2)Machine Learning / Data Science->model train before weight initializaton 



# array od ones
# one_array=np.ones((2,3))
# print(one_array)
# so in this case it will give 2 row and 3 column  with 1 array like [[1. 1. 1.] [1. 1. 1.]] 
# method=np.ones(shape)
# parameter=(row,column)/shape
# applications=1)testing program=its use program test for dummy data 
            # 2)matrix operation=ones array is used for matrix operation or calculation



# arange array
# range_array=np.arange(1,11,2)
# print(range_array)
# it give range 1 to 10 with 2 step like 1,3,5,7,9
# method=np.arrange(start,end,step)
# parameter=start,end,step
# in thus ex:starting point is 1 ,end is 11 so its run on 10 and its step is 2 so is give numbers with 2 step
# application 1)generate number in sequence
            # 2)for even/odd numbers


# range_array=np.arange(11,1,-2)
# print(range_array)
# is this same but it will work decrement



# basic mathematical operation
# array1=np.array([1,2,3,4])
# array2=np.array([5,6,7,8])
# print("addition:",array1+array2)
# print("sub:",array2-array1)
# print("mul:",array1*array2)
# print("div:",array1/array2)
# so we will create all oeparation without crating loop 
# methods=   +,-,*,/
# parameter=array1,array2
# application= 1)in the dataset we can apply add,mul,sub,div
            #  2) in the ml weight and feature mul 


# <!-- # 9. In-Class Practice Problems

# Students should attempt the following during the lecture.
# Problem 1:
# Create a NumPy array containing numbers from 1 to 20.
# array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,11,13,14,15,16,17,18,19,20])
# print(array)


# Problem 2:
# Create a 3x3 matrix with values from 1 to 9.
# array=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(array)

# we will create also this type
# array1=np.arange(1,10).reshape(3,3)
# print(array1)

# Problem 3:
# Multiply every element of an array by 10.
# array=np.array([1,2,3,4])
# print("mul by 5",array*5)


# Problem 4:
# Find the shape and dimension of a 4x5 zero matrix. -->
# array=np.zeros((4,5))
# print(array)
# print(array.shape)
# print(array.ndim)


# We understood:

# - What is an array
# ----->array means collecting the same datatype element
# - Why NumPy is required
# ----->numpy is required because normal python lis are slow
    #     and take more memory and its not support mathematecal opertaion easily but numpy salove this problem

# - How to create NumPy arrays
# ------->np.array(),np.arange(),np.zeros(),np.ones(),np.empty(),np.random.randint(1,10,(3,3)),np.full((3,3),7),np.eye(4)

# - Difference between list and array
# ----->list is store differnt data type and array store only same data type
        # list speed is slow and array speed is very fast
        # list takes more memory and array uses less memory
        # list dose not support direct math but array spport direct math operation

# - Vectorized operations
#  ----->Vectorized operation means instead of using loops that work with each element one-by-one, NumPy performs the operation on the entire array at the same time.

# - Multi-dimensional arrays
# ----->A multi-dimensional array is an array that has more than one dimension (rows, columns, depth). In NumPy, these arrays are called ndarrays.

# - Array properties
# ---->there are maany property like ndim,shape,size,dtype,itemsize,nbytes,t-transpose,flat,real & imag
#        | Property   | Meaning              |
# | ---------- | -------------------- |
# | `ndim`     | Number of dimensions |
# | `shape`    | Rows × Columns       |
# | `size`     | Total elements       |
# | `dtype`    | Data type            |
# | `itemsize` | Bytes per element    |
# | `nbytes`   | Total bytes          |
# | `T`        | Transpose            |
# | `flat`     | 1D iterator          |

# - Basic mathematical operations
# 1. Addition (+)   2. Subtraction (-)   3. Multiplication (*)    4. Division (/)  
#  5. Modulus (%)   6. Exponent / Power (**)   7. Floor Division (//)



# np,linespace===means crate evenly spaced between tow limite like we have 2 limite 0 to 4 so we will used od linespase we will 0 to 4 in one line to equal parts
## Syntax

# np.linspace(start, stop, num=50, endpoint=True, dtype=None)

## Parameters
# - start → starting value
# - stop → ending value
# - num → number of samples
# - endpoint → include stop value or not
# - dtype → optional data type
## Advantage

# - Guarantees fixed number of points
# - Useful in plotting and numerical analysis

# application=1)data visulization=its use data pointe make
            # 2)graph ploating=its use for make gtraph to give equally value  


# # example
# arr = np.linspace(0, 4, 5)
# print(arr)
# array=np.linspace(1,10,3,dtype=int)
# print(array)


# np.logspace()
# in this method it is create equal part in logarithmic scale
## Syntax
# np.logspace(start, stop, num=50, base=10.0)
## Parameters
# - start → exponent start
# - stop → exponent stop
# - num → number of samples
# - base → logarithmic base
## Advantage
# - Essential for exponential growth modeling
# - Used in frequency 

# application=1)graph ploatong =for use log base grapg make  

# # example
# arr = np.logspace(1, 3, 4)
# print(arr)


#   np.empty
# --->create an array without initialing entires and is faster than zeros and ones because values not  assigned 
# arr = np.empty((3,3))
# print(arr)
# method=np.empty(shape)
# parameter=(row,column)/shape
# empty have not initially value but its store random values
# application= 1)fast memory allocation its crate array speedly than zeros or ones
            #  2)data proccesing=its make structure before the data procceing




# np.eye() and np.identity()====>to create a identity matrices used in liner algebra and matrix operation
## Syntax
# np.eye(N, M=None)
# np.identity(n)
# Parameters:
# - N → number of rows
# - M → columns (optional)
# Advantage:
# - Essential in matrix multiplication
# - Used in solving linear equations
# | Function        | Matrix Type                      |
# | --------------- | -------------------------------- |
# | `np.eye()`      | its also make Rectangular matrix |
# | `np.identity()` | only square matrix               |

# # application
#1) Identity matrix 
#2) Matrix multiplication
#3) Linear algebra calculations

# print(np.eye(4,4))
# print(np.identity(3))



# random array eneration

# Why random arrays exist?
# - Simulations
# - Machine learning
# - Statistical experiments
# - Testing algorithms

# np.random.rand()
# Uniform distribution [0,1)
# Syntax:
# # np.random.rand(size)
# np.random.rand() creates an array of random numbers between 0 and 1 (floating-point values).
# ✔ All values are ≥ 0 and < 1
# ✔ Numbers are uniformly distributed
# ✔ You can create 1D, 2D, or multi-dimensional arrays
# method=np,random.rand(size)
# parameter=size=how many values
# application=for randon data generate or create random dataset



# np.random.randn()
# Normal distribution (mean=0, std=1)
# Syntax:
# np.random.randn(size)
# np.random.randn() generates random numbers from a:
# Standard Normal Distribution
# Mean (μ) = 0
# Standard deviation (σ) = 1
# Values include negative, zero, positive
# This is different from rand(), which gives only 0 to 1 positive values.
# method=np.random.randn(size)
# parameter=size=how many values
# application=for randon data generate or create random dataset



# ## np.random.randint()
# Random integers
# Syntax:
# # np.random.randint(low, high, size)
# np.random.randint() generates random integers (whole numbers) within a given range.
# method=np.random.randint(start,end,size)
# parameter
# low → starting number (inclusive)
# high → ending number (exclusive)
# size → shape of array (optional)
# application=for randon data generate or create random dataset



## np.random.choice()
# Random sampling
# Syntax:
# np.random.choice(a, size=None)
# np.random.choice() selects random values from a given list, array, or range.
# You can choose:
# One value
# Multiple values
# With replacement (repeat allowed)
# Without replacement (no repeat)
# method= np.random.choice(a, size=None)
# parameter=arrayname,size=how many you will take
# application=its select the random sample from the dataset



# ## np.random.seed()
# Ensures reproducibility
# Syntax:
# # np.random.seed(seed_value)
# np.random.seed() is used to fix the randomness so that you get the same random numbers every time you run the code.
# In short:
# Seed = repeatable results
# Without seed → results change every time
# With seed → results stay the same
#  np.random.seed()
# application=stable value 



# example:
# np.random.seed(42)
# print("uniform",np.random.rand(2,3))
# print("normal",np.random.randn(2,2))
# print("random integer",np.random.randint(1,10,(2,3)))
# print("random choice:",np.random.choice([10,20,30],size=9))


# array=np.array([[5,6,7,8],[1,2,3,4]])
# print(array.itemsize)
# size of one element in byte
# print(array.nbytes)
# nbytes is give total memory consumed





# reshapping method
# reshape():==change dimensions without changing data
# if we have any of the matrix so this is change the dimenssion means row and column without changing  data1
# method=.reshape(row,column)
# parameter=row,column/shape


# # ravel():==return flattened array(viwe).
# ravel() returns a flattened array, meaning it converts a multi-dimensional array (2D/3D) into a 1D array.
# ravel() returns a view, not a copy.
# So changing the flattened array will also change the original array.
# method=.ravel

# # flatten():==returns flattened copy
# flatten() returns a flattened COPY of the array.
# It converts any multi-dimensional array (2D/3D) into a 1D array, but unlike ravel(), it does NOT return a view.
# ✔ flatten() → returns a copy
# ✔ Changing the flattened array does NOT affect the original array
# method=.flatten()


# shape():==changes shape permanently
# method=.shape(row,column)
# parameter=.shape(row,column)

# array1=np.arange(1,10)
# print(array1)

# reshaped=array1.reshape(3,3)
# print("reshaped:\n",reshaped)

# print("ravel:",reshaped.ravel())
# print(array1)

# print("flatten:",reshaped.flatten())
# print(array1)

# array1.resize(3,3)
# print("resize:\n",array1)

# print(array1)




# transpose:==it is transpose row to column and column to row
# method
# arr.T:==shortcut for transpose
# method=array_name.T
# np.transpose(arr):==explicit transpose function used to swap rows and column
# method=np.transpose(array_name)
# parameter=array_name



# matrix=np.array([[1,2,3],[4,5,6]])
# print("original:\n",matrix)
# print("tramnspose using T:\n",matrix.T)
# print("transpose using function:\n",np.transpose(matrix))


# array operation
# Array operations are the core strength of NumPy.
# Why do we need array operations?
# Because in scientific computing and machine learning we frequently perform:
# Element-wise arithmetic
# Comparisons
# Logical filtering
# Mathematical transformations
# NumPy allows these operations without explicit loops. This is called vectorization.


# arithmetic operation
# 1.addition,2.subtraction,3.multiplication
# 4.division,5.floor division,6.power,7.modulo
# parameter=a,b
# a=np.array([10,20,30])
# b=np.array([2,4,5])
# print("addition:",a+b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Power:", a ** 2)
# print("Modulus:", a % b)
# in this case we have 2 array and this operation work is 
# first variable array of 1 number is add with second variable of 1 numbers and all them

# Why these operators exist:
    # Enable vectorized computation
    # Avoid explicit loops
    # Faster execution due to C backend
    # Memory efficient

# comparision operator
# it is used for element wise comparision
# 1.>graterthsn,2.<lessthan3.>=graterthan or equalto
# 4.<=lessthan or equalto 5.==doubbel equalto

# a=np.array([10,20,30])

# print("only boolean value")
# print("graterthan",a>20)
# print("lessthan",a<20)
# print("grater or equal",a>=20)
# print("less or equal",a<=20)
# print("doubl equal",a==20)

# print("numbers wich is true")
# print("graterthan",a[a>20])
# print("lessthan",a[a<20])
# print("grater or equal",a[a>=20])
# print("less or equal",a[a<=20])
# print("doubl equal",a[a==20])


# logical operation
     # it is used when we have two or more conditions

# functions::
    # parameter=conditionm
    # np.logical_and(condition1,condition2)
    # np.logical_or(condition1,condition2)
    # np.logical_not(condition)

# Why these exist:
  # Combine Boolean conditions
  # Enable complex filtering
  # Used heavily in data analysis

# a=np.array([5,10,15,20])
# con1=a>8
# con2=a<18

# print("for boolean")
# print("logical and",np.logical_and(con1,con2))
# print("logical or",np.logical_or(con1,con2))
# print("logical not",np.logical_not(con1))

# print("for numbers")
# print("logical and",a[np.logical_and(con1,con2)])
# print("logical or",a[np.logical_or(con1,con2)])
# print("logical not",a[np.logical_not(con1)])


# element wise aggregate operation
# element wise operation is applied to each element individualy
# aggregate is reduce array to single value
# array=np.array([1,2,3,4])
# print("power",array**2)
# print("sum",np.sum(array))
# soin this method is work all element wise operation so its all to power and then its sum of the total values of array



#session 5:::Basic mathematical function
# =======================================
# NumPy provides optimized mathematical functions.
# Why separate functions exist when operators already work?
# Because:
# Functions allow explicit usage
# Useful in functional programming
# More readable in complex expressions
# Support broadcasting and advanced parameters
#  Functions:
# np.add()
# parameter=array1,array2
# =====addition all elemnt wise

# np.subtract()
# parameter=array1,array2
# ====subtract all elements wise

# np.multiply()
# parameter=array1,array2
# =====multiply all element wise

# np.divide()
# parameter=array1,array2
# ======divide all element wise

# np.power()
# parameter=array1**value
# ======its give power of the all element

# np.mod()
# parameter=array1,array2
# ====modulo operation of all element wise

# np.sqrt()
# parameter=array1
# ====its give squre root of the all elements

# np.exp()
# parameter=value
# =====its give exponential values

# np.log()
# parameter=array1
# ====its give all elemnet wise log base 2

# np.log10()
# parameter=array1,array2
# =====its give all element wise log base 10

# np.round()
# parameter=array1
# ====its give rounded values


#c=np.array([10.2,20.6,30.5]) if we have this array so its give round values of 10,21,30
# np.floor()
# parameter=array1
# ==== its give flooring values

# c=np.array([10.2,20.6,30.5]) if we have this array sor its give floor of the values like 10,20,30
# np.ceil()
# parameter=array1
# its give ceil values

# c=np.array([10.2,20.6,30.5]) if we have this array so its give ceil valu like 11,21,31

# practicals of basic mathematical functions
# a=np.array([4,9,16])
# b=np.array([2,3,4])
# print("add",np.add(a,b))
# print("subtract",np.subtract(a,b))
# print("multiply",np.multiply(a,b))
# print("divide",np.divide(a,b))
# print("power",np.power(a,2))
# print("mod",np.mod(a,b))

# print("square root",np.sqrt(a))
# print("exponential",np.exp(1))
# print("natral log",np.log(a))
# print("natral log",np.log10(a))

# c=np.array([10.2,20.6,30.5])
# print("round",np.round(c))
# print("floor",np.floor(c))
# print("ceil",np.ceil(c))


# Statistical operations reduce arrays.
# Functions:
# np.mean()==mean of the values   #paramter=array_name
# np.median()===median of the values    #paramter=array_name
# np.std()==standard deviation    #paramter=array_name
# np.var()==variance         #paramter=array_name
# np.min()=min value         #paramter=array_name
# np.max()==max value of the given values      #paramter=array_name
# np.sum()=sum of the all values         #paramter=array_name
# np.cumsum()==cumulative sum like [10, 20, 30, 40, 50] this array to                  #paramter=array_name
#                     first=10,second=10+21=30,third=second+third=30+30=60.....
# np.prod()=product of the values  #paramter=array_name
# np.percentile()==give percentile    #paramter=array_name,percentile
# Why these exist:
# Data analysis
# Machine learning preprocessing
# Performance metrics

# practicals of statistical operation 
# data=np.array([10,20,30,40,50])
# print("mean",np.mean(data))
# print("median",np.median(data))
# print("standard deviation",np.std(data))
# print("varriance",np.var(data))
# print("minimum",np.min(data))
# print("maximum",np.max(data))
# print("sum",np.sum(data))
# print("cumulative sum",np.cumsum(data))
# print("90 th persentile",np.percentile(data,90))
# print("product",np.prod(data))




# swssion 6::indexing & slicing in numpy
# ========================================

# indexing and slicing are fundamental for
    # access specific element
    # extract subset of data
    # filtering dataset
    # modifying portion of array


# 1 basic indexing (1D)
# to access individual elememt from an array
# syntax=arr[index]
# index start from 0

# arr=np.array([10,20,30,40])
# print("elememt at index",arr[0])
# print("elememt at index",arr[2])


# 2 negative indexing::
# to access element from the end of the array
# arr[-1]->last elememt
# arr[-2]->second last element

# arr=np.array([10,20,30,40])
# print("last element",arr[-1])
# print("second last element",arr[-2])

# 3 basic indexing (2d array)
# to access element in matrices
# syntax::arr[row_index,column_index]
# matrix=np.array([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]])
# print("element at (1,2):",matrix[1,1])



# 4 slicing::
# to extract subarrays.
# syntax:arr[start:stop:step]
    # start -> inclusive
    # stop ->exclusive
    # step ->interval

# arr=np.array([0,10,20,30,40,50])
# print("slicing 1:4",arr[1:4])
# print("slicing with step 2",arr[0:6:2])



# 5::2d slicing
# syntax->arr[row_start:row_end,col_end]
# matrix=np.array([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]])
# print("submatrix:\n",matrix[0:2,1:3])
# print(matrix[0:2])
# print(matrix[0:3,1:3])


# 6 boolean indexing 
# to filter arrays based on condition
# syntax->arr[condition]

# arr=np.array([5,10,15,20])
# print("element>10",arr>10)
# print("elments>10",arr[arr>10])


# 7::indexing with np.where()
# to get indices where condition is true
# syntax->np.where(condition)
# parameter=condition
# arr=np.array([5,10,15,20])
# indices=np.where(arr>10)
# print("indices:",arr[indices])



# session :7==array manipulation
# ===============================


# Array manipulation functions are essential when:
# Combining datasets
# Splitting data for training/testing
# Modifying array structure
# Adding or removing elements
# Managing memory correctly

# 1. np.concatenate()
# parameter=arra1,array2,axis
# Why It Exists
# To join arrays along an existing axis.
# Syntax
# np.concatenate((arr1, arr2), axis=0)
# Parameters
# tuple of arrays → arrays to combine
# axis → 0 (rows), 1 (columns)
# Important
# Arrays must have same shape except along concatenation axis.

# # exampale
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# print("Concatenate axis=0:\n", np.concatenate((a,b), axis=0))
# print("Concatenate axis=1:\n", np.concatenate((a,b), axis=1))




# 2. Stacking Functions
# Stacking adds a new dimension or stacks arrays in specific orientation.
# np.vstack()
# Vertical stacking (row-wise)
# np.hstack()
# Horizontal stacking (column-wise)
# keyboard_arrow_down 
# np.dstack()
# Depth stacking (third dimension)


# example
# print("vstack:\n", np.vstack((a,b)))
# print("hstack:\n", np.hstack((a,b)))
# print("dstack:\n", np.dstack((a,b)))


# Stacking vs Concatenation
# Concatenation:
# Joins along an existing axis.
# Stacking:
# May introduce new axis (especially dstack).
# Use stacking when creating higher dimensional arrays.





# 3. Splitting Arrays
# np.split()
# Splits array into equal parts.
# Syntax: np.split(arr, sections, axis=0)
# parameter=arr, sections, axis
# np.array_split()
# parameter=arr, sections, axis
# Allows unequal splitting.
# Why two functions?
# np.split() requires exact division. np.array_split() handles uneven splits.

# exmple
# arr = np.arange(8)
# print(arr)
# print("Split:", np.split(arr, 4))
# print("Array Split:", np.array_split(arr, 3))



# 4. Insert, Append, Delete
# np.insert(arr, index, values, axis=None)
# parameter=arr, index, values, axis
# Inserts values before given index.

# np.append(arr, values, axis=None)
# parameter=arr, index, values, axis
# Appends values at end.

# np.delete(arr, index, axis=None)
# parameter=arr, index, values, axis
# Deletes elements at index.
# Important: These return new arrays (original not modified).

# example::
# arr = np.array([10,20,30])
# print("Insert:", np.insert(arr, 1, 15))
# print(arr)
# print("Append:", np.append(arr, 40))
# print(arr)
# print("Delete:", np.delete(arr, 1))
# print(arr)


# 5. Copy vs View
# Understanding memory behavior is critical.
# View (.view())
# Shares memory with original array.
# Copy (.copy())
# Creates independent memory.
# Modifying view affects original. Modifying copy does not



# example
# arr = np.array([1,2,3])
# view_arr = arr.view()
# copy_arr = arr.copy()
# arr[0] = 100
# print("Original:", arr)
# print("View:", view_arr)
# print("Copy:", copy_arr)





# session - 8 useful utility funcion in numpy
# =============================================
# utility function in numpy help perform  common operation required in data
#   processing and analysis 


# these function are widely used for
    #   1.data cleaning
    #   2.sorting data
    #   3.indentifying missing values
    #   4.checking logical condition
    #   5.handling spicial values such as NaN and infinity
# in this session we will study:
    #   1.np.unique()
    #   2.np.sort() and np.argsort()
    #   3.np.where()
    #   4.np.nonZero()
    #   5.np.any() and np.all()
    #   6.np.isnan(),np.isinf(),np.isfinite()
    #   7.np.clip()
    #   8.handling NaN values




# data inspection
# 1.np.unique()

# purpose: return the unique elements of an array by removing duplicate values
# syntax:np.unique(array)
# parameter:input array
# return array of unique values
# example
# arr=np.array([1,2,2,3,3,4,5,5])
# print(np.unique(arr))

# 2.sorting function
#  sorting is important in data preprocessing and statistical analysis
# numpy provide two useful function
# 1.np.sort()
# 2.np.argsort()

# 1.np.sort()
# return a sorted copy of the array
# syntax:np.sort(array)
# parameters:array:input array
# return sorted array
# example
# arr=np.array([30,10,50,20])
# print(np.sort(arr))

# 2.np.argsort()
# insted of returning sorted values,this function return the indices that would sort the array.
# syntax:np.argsort(array)
# parameter:array:input array
# return indices of element in sorted order
# example
# arr=np.array([30,50,10,20])
# print(arr)
# print("indices",np.argsort(arr))


# ====
# conditional operation
# 3.np.where()
# it is used to find indices where a condition is true
# it is very useful for conditional selection and filtering
# syntax:np.where(condition)
# return:indices where the condition is satisfide
# example:
# arr=np.array([5,10,15,20,25])
# print(np.where(arr>15))
# print(arr[np.where(arr>15)])



# conditional operation
# 4.np.nonZero():
# this function return the indices os non-Zero element
# syntax:np.nonzero(array)
# return:indices of element that are not equal to zero
# example:
# arr=np.array([0,1,0,2,3,0])
# print(np.nonzero(arr))



# logical check
# 5.no.any() and np.all():
# these function are used to check logical condition or array

# 1.np.any()
# return True if at least one element satisfies the condition.
# syntax:np.any(condition)

# 2.np.all():
# return true only if all elements satisfy the condition.
# syntax:np.all(condition)
# example:
# arr=np.array([5,10,15])
# print("any elements grater tha 12:",np.any(arr>12))
# print("all elements grater tha 12:",np.all(arr>12))



# special value detection
# 6.checking special values:
# real-world dataset often contain special values such as:
# 1.NaN(not a number)
# 2.infinity
# 3.negative infinity
# numpy provide function to identify them.

# 1.np.isnan():
# check whether elements are NaN.
# 2.np.isinf():
# checks whether elements are infinite.
# 3.np.isfinite():
# checcks whether elements are finite values.

# example:
# arr=np.array([1,np.nan,np.inf,-np.inf,5])
# print(arr)
# print("isnan",np.isnan(arr))
# print("isinf",np.isinf(arr))
# print("isfinite",np.isfinite(arr))



# value limiting
# 7.np.clip():
# np.clip() limits values within a specified range.
# values below the minimum are replaced with the minimun values.
# values above the maximum are replaced with the maximum values
# syntax:np.clip(array,min_val,max_val)
# example:
# arr=np.array([2,5,10,15,20])
# print(arr)
# print(np.clip(arr,5,15))


# 8.Handling NaN values:
# NaN stands for "Not a number"
# it is used to represent missing or undefined values.
# example:np.nan
# standard stastistical function return NaN if the dataset contains NaN values.
# to handel this,numpy provides special function
# 1.np.nanmean()
# 2.np.nanstd()
# 3.np.nansum()
# these function ingnore NaN values during computation.
# example:
# arr=np.array([10,20,np.nan,40])
# print(arr)
# print("mean(normal):",np.mean(arr))
# print("mean ingnoring NaN:",np.nanmean(arr))
# print("standard deviation ingnoring NaN:",np.nanstd(arr))
# print("sum ingnoring NaN:",np.nansum(arr))

