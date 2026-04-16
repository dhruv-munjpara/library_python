import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9,10])
condition1=array>2
condition2=array<8
print("logical and",np.logical_and(condition1,condition2))
print("logical and",array[np.logical_and(condition1,condition2)])
condition3=array>10
condition4=array<3
print("logical and",np.logical_or(condition3,condition4))
print("logical and",array[np.logical_or(condition3,condition4)])

print("logical and",np.logical_not(condition3))
print("logical and",array[np.logical_not(condition3)])