# import the numpy 
import numpy as np

# np.array(object/list,dtype=none)

# parameter=object/list/tuple -is this convert data to array
            #dtype is this optional it's define the type of the data 
# application=1.mathematical operation or fast calcylation
            # 2.ml or datascince in this ml dataset is store in the array
            # 3.matrix opertion in the matrix calculation linear algebra is use this
            # 4.image proccesing is this image is store in array
            # 5.data manipulation its use in data filtering,indexing



# Explanation:
# shape → (rows, columns)
# ndim → number of dimensions->1 demention
# size → total elements in array->how many elemnt are there in the array its the givr size of the array
# dtype → data type of elements->ite give the type of the data


# array of zeros
#np.zeros(shape,dtype=float):
# it this one of the array which is store the all zero values

# parameter=(row,column/shape,dtype=float):
# its make size or dimension and dtype is optional its definr data type

# application=1.Initialize array for calculations,matrix operations
            # 2.Machine Learning / Data Science->model train before weight initializaton 
            # 3.image procesing use of image pixel array initialize
            # 4.scientific computing/simulation :its use before start the simulation make a empty structure

# array od ones
# np.ones(shape,dtype=float)
# its make one array which values is all one
# parameter=(row,column)/shape,dtype=float=optional
# applications=1.Initialize array for calculations,matrix operations
             # 2.Machine Learning / Data Science->model train before weight initializaton 
             # 3.image procesing use of image pixel array initialize
             # 4.scientific computing/simulation :its use before start the simulation make a empty structure




# arange array
#np.arange(start,stop,step,dtype):
# its make array with range of numbers
# its same as python range but its return numpy array
# parameter=1️start → starting number (optional, default = 0)
          # 2️. stop → ending number 
          # 3️. step → numbers between gap
          # 4️. dtype (optional) → data typ
# application 1)generate number in sequence
            # 2)for even/odd numbers
            # 3)looping/iteration:its use index values generate 
            # 4)data scince/ml:its use generate data indexes or feature value
            # 5)graph ploatting:it use in X-axis values generate(matplotlib). 


 
# methods=   +,-,*,/
# parameter=array1,array2
# application= 1)in the dataset we can apply add,mul,sub,div
            #  2) in the ml weight and feature mul
            #  3)in ml model training vector calculations 
            #  4)image proccessing:it use in  operation of image pixels



# | ---------- | -------------------- |
# | `ndim`     | Number of dimensions |
# | `shape`    | Rows × Columns       |
# | `size`     | Total elements       |
# | `dtype`    | Data type            |
# | `itemsize` | Bytes per element    |
# | `nbytes`   | Total bytes          |
# | `T`        | Transpose            |
# | `flat`     | 1D iterator          |



# np,linespace===means crate evenly spaced between tow limite like we have 2 limite 0 to 4 so we will used od linespase we will 0 to 4 in one line to equal parts

# np.linspace(start, stop, num=50, endpoint=True, dtype=None)

## Parameters
# - start → starting value
# - stop → ending value
# - num → number of samples
# - endpoint → include stop value or not
# - dtype → optional data type
## application:1.graph ploting
              #2.ml testing data its use in continuous values generate   
              #3.simulation:it equal interval values
              #4.data scince:time intervals/ranges generate   


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
            # 2)ml/data science= hyperparameter test and log scale values generate
            # 3)engineering calculations=its use for large range numbers represent 


#   np.empty
# --->create an array without initialing entires and is faster than zeros and ones because values not  assigned 
# method=np.empty(shape,dtype)
# parameter=(row,column)/shape , dtype → data type (optional)
# application= 1)fast memory allocation its crate array speedly than zeros or ones
            #  2)data proccesing=its make structure before the data procceing



# np.eye() and np.identity()====>to create a identity matrices used in liner algebra and matrix operation
#method=np.eye(N,M,K,dtype)
# Parameters
# N → rows
# M → columns (optional)
# k → diagonal index
# dtype → data type

# np.identity(n)
# Parameters:
# - N → number of rows

# Advantage:
# - Essential in matrix multiplication
# - Used in solving linear equations
# | Function        | Matrix Type                      |
# | --------------- | -------------------------------- |
# | `np.eye()`      | its also make Rectangular matrix |
# | `np.identity()` | only square matrix               |
# | `np.eye()`      | rows and columns different  |
# | `np.eye()`      | diagonal shift (`k`) support|
# | `np.identity()` | simple identity matrix      |

# # application
#1) ml/data science-its use matrix calulation in algorithms
#2) Matrix multiplication
#3) Linear algebra calculations-in the matrix mul we can use identity matrix





# random array eneration

# Uniform distribution [0,1)
# Syntax:np.random.rand(size)
# parameter=size=how many values,row,column
# application=1)ml-for randon data generate or create random dataset
#             2)data simulation-we can make dummy data
#             3)testing algorithms-rendam input data to algorithm test
#             4)scientific experiments-probability simulation and statistical testing


# Normal distribution (mean=0, std=1)
# Syntax:np.random.randn(size)
# Standard Normal Distribution
# Mean (μ) = 0
# Standard deviation (σ) = 1
# Values include negative, zero, positive

# parameter=size=how many values,row,column
# application=1)for randon data generate or create random dataset
            # 2)ml-neural networks in weight initialization
            # 3)statistics/data science-use of normal distribution data simulation


# Syntax:np.random.randint(low, high, size)
# parameter
# low → starting number (inclusive)
# high → ending number (exclusive)
# size → shape of array (optional)
# application=1)for randon data generate or create random dataset
#             2)ml/data science-its use in ml or data science make a dummy integer dataset generate
#             3)testing programs-it use of algorithms test


# Syntax:np.random.choice(a, size=None)
# parameter=arrayname,size=how many you will take
# application=1)its select the random sample from the dataset
#             2)ml-we can selecting random data in training and testing
#             3)simulation-random event generate



# Syntax:np.random.seed(seed_value)
# np.random.seed() is used to fix the randomness so that you get the same random numbers every time you run the code.
# In short:
# Seed = repeatable results
# Without seed → results change every time
# With seed → results stay the same
# application=1)stable value 
#             2)model testing-use when we can testing a algorithms so its give same random dataset generate
#             3️)Research & Experiments-in the scientific research consistent result maintain
            # 4)debugging-same random numbers get when program errors check




# reshapping method
# reshape():==change dimensions without changing data
# if we have any of the matrix so this is change the dimenssion means row and column without changing  data1
# method=.reshape(row,column)
# parameter=row,column/shape
# application:-1)ml-we can use of dataset for model training to convert in proper shape
#              2)image processing-image data reshape(pixels matrix)
#              3)matrix-linear algebra calculations 


# # ravel():==return flattened array(viwe).
# ravel() returns a flattened array, meaning it converts a multi-dimensional array (2D/3D) into a 1D array.
# ravel() returns a view, not a copy.
# method=.ravel()


# # flatten():==returns flattened copy
# flatten() returns a flattened COPY of the array.
# It converts any multi-dimensional array (2D/3D) into a 1D array, but unlike ravel(), it does NOT return a view.
# flatten() → returns a copy
# Changing the flattened array does NOT affect the original array
# method=.flatten()

# application of ravel() and flatten()
# 1)ml-we can convert the dataset for model training in 1d formate
# 2)image processing-we can convert image matrix to vector form
# 3)data analysis-we can use of array operation make very easy


# # shape():==changes shape permanently
# method=.shape(row,column)
# parameter=.shape(row,column)
# application:-1)data science/ml-we can see row and column of the dataset
#              2)data validation-we can check the size before model tarin
#              3)reshaping array-we can check coorect dimensions before use reshape()



# transpose:==it is transpose row to column and column to row
# method=array_name.T
# np.transpose(arr):==explicit transpose function used to swap rows and column
# method=np.transpose(array_name)
# parameter=array_name
# application:-
# 1)linear algebra=matrix operation
# 2)ml=dataset orientation change
# 3)data analysis=row to column and column to rows convert


# arithmetic operation
# 1.addition,2.subtraction,3.multiplication
# 4.division,5.floor division,6.power,7.modulo
# application:-
# 1)data science=dataset calculation
# 2)ml=vector and matrix computations.
# 3)scientific computing



# comparision operator
# it is used for element wise comparision
# 1.>graterthsn,2.<lessthan3.>=graterthan or equalto
# 4.<=lessthan or equalto 5.==doubbel equalto
# application:-
# 1)data filtering-condition wise data select
# 2)ml=in the dataset check the condition
# 3)data cleaning=invalid values identity


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
# application:-
# 1)data filtering
# 2)data celaning
# 3)ml=check dataset condition



#session 5:::Basic mathematical function
# =======================================
#  Functions:
# np.add()
# parameter=array1,array2
# appliction:-
# 1)data science=values add 
# 2)ml=vector and computations
# 3)image proccening=add pixel values of images
# =====addition all elemnt wise


# np.subtract()
# parameter=array1,array2
# application:-
# 1)data science=we can calculate different btwn dataset
# 2)ml=we can calculate prediction error calculate
# 3)image processing=find difference btwn image pixel
# ====subtract all elements wise


# np.multiply()
# parameter=array1,array2
# application:-
# 1)ml-feature and weight mul 
# 2)ds-calculation on dataset
# 3)image-proccessing=pixel scaling
# =====multiply all element wise

# np.divide()
# parameter=array1,array2
# application:-
# 1)ds-find ratio or percentile
# 2)ml-normalization/scalling
# 3)image-procceing=pixel normalization
# ======divide all element wise

# np.power()
# parameter=array1**value
# application:-
# 1)ml-fetuare tranformation
# 2)ds-groth calculation
# ======its give power of the all element

# np.mod()
# parameter=array1,array2
# application:-
# 1)even/odd check
# 2)ds-pattern detection
# ====modulo operation of all element wise

# np.sqrt()
# parameter=array1
# application:-
# 1)ds-distance calculation
# 2)ml-use in normalization and dormulas
# ====its give squre root of the all elements

# np.exp()
# parameter=value
# application:-
# 1)ml
# 2)ds-exponential groth calculation
# =====its give exponential values

# np.log()
# parameter=array1
# application:-
# 1)datacleaning=drop extra decimal value
# 2)ml=make prediction readable
# ====its give all elemnet wise log base 2

# np.log10()
# parameter=array1,array2
# application:-
# 1)datacleaning=drop extra decimal value
# 2)ml=make prediction readable
# =====its give all element wise log base 10

# np.round()
# parameter=array1
# application:-
# 1)datacleaning=drop extra decimal value
# 2)ml=make prediction readable
# ====its give rounded values

# np.floor()
# parameter=array1
# ==== its give flooring values

# c=np.array([10.2,20.6,30.5]) if we have this array sor its give floor of the values like 10,20,30
# np.ceil()
# parameter=array1
# its give ceil values


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

# Applications of NumPy Statistical Functions
# 1)data analysis-understand row data
# 2)ml=analyze the data before model train
# 3)data celaining=wrong or missing value handle
# 4)probability & static
# 5)data visualization=data summarize before make a graphs


# swssion 6::indexing & slicing in numpy
# ========================================

# indexing and slicing are fundamental for
    # access specific element
    # extract subset of data
    # filtering dataset
    # modifying portion of array


# 7::indexing with np.where()
# to get indices where condition is true
# syntax->np.where(condition)
# # parameter:-
# condition → True/False condition
# x → if condition True so print value
# y → if condition False so print valu
# application:-


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
# application:-
# 1)ds=its combaine diff dataset
# 2)ml=train+test data combine
# 3)image procceing=its joint image to side-by-side


# 2. Stacking Functions
# Stacking adds a new dimension or stacks arrays in specific orientation.
# np.vstack()
# Vertical stacking (row-wise)
# np.hstack()
# Horizontal stacking (column-wise)
# keyboard_arrow_down 
# np.dstack()
# Depth stacking (third dimension)
# application:-
# 1)ds=merge multiple dataset
# 2)ml=combine feature(hstack)


# np.array_split()
# parameter=arr, sections, axis
# Allows unequal splitting.
# Why two functions?
# np.split() requires exact division. np.array_split() handles uneven splits.
# application:-
# 1)ml=make datset training and testing
# 2)batch proceing


# 4. Insert, Append, Delete
# np.insert(arr, index, values, axis=None)
# parameter=arr, index, values, axis
# Inserts values before given index.
# application:-
# 1)data correction=its add worng place value
# 2)ml=ake new feature insert

# np.append(arr, values, axis=None)
# parameter=arr, index, values, axis
# Appends values at end.
# application:-
# 1)data collection=add new Data
# 2)dataset expansion=incress ml dataset

# np.delete(arr, index, axis=None)
# parameter=arr, index, values, axis
# Deletes elements at index.
# Important: These return new arrays (original not modified).
# application:-
# 1)data celaning=remove unwantade Value
# 2)outlier removal=remove wrong or extream value
# 3)ml=remove unnecessary column


# 5. Copy vs View
# Understanding memory behavior is critical.
# View (.view())
# Shares memory with original array.
# application:-
# 1)memory optimization=its avoid extra memory in large dataset
# 2)fast processing=fast operation ,should not make copy
# 3)data sharing=use in same data multiple  variable 


# Copy (.copy())
# Creates independent memory.
# Modifying view affects original. Modifying copy does not
# application:-
# 1)safe data modification=work without cahnge original dataset
# 2)ml=safe original values
# 3)datacelaning=avoid original data loss in cealing Process


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
# application:-
# 1)data celaing=remove duplicate Value
# 2)ml=category Value identity
# 3)data validation=check duplicate



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
# application:-
# 1)da=organize data
# 2)ml=ranking importance
# 3)data visualization=sorted data for graphs

# 2.np.argsort()
# insted of returning sorted values,this function return the indices that would sort the array.
# syntax:np.argsort(array)
# parameter:array:input array
# return indices of element in sorted order
# applications:-
# 1)ranking=define value ranking
# 2)ml=pridiction rank or feature importance sorting


# ====
# conditional operation
# 3.np.where()
# it is used to find indices where a condition is true
# it is very useful for conditional selection and filtering
# syntax:np.where(condition)
# return:indices where the condition is satisfide



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
# applications:-
# 1)data validation=chack value valid or not
# 2)ML=MODEL INPUT VALIDATION


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
# application:-
# 1)data cleaing=remove nan and infinite
# 2)misiing value detection=identity missing Value
# 3)ml=remove invalid value befor model train
# 4)data validation=check data is all celan or not


# value limiting
# 7.np.clip():
# np.clip() limits values within a specified range.
# values below the minimum are replaced with the minimun values.
# values above the maximum are replaced with the maximum values
# syntax:np.clip(array,min_val,max_val)
# application:-
# 1)data cleaning=outliers control
# 2)ml=feature scaling/normalization
# 3)image processing=limit the pixel value


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
# application:-
# 1)missing data handling=calculation of incomplate data
# 2)data cleaning=ignore nan values
# 3)ml=handel the missing value before training

