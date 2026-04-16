import numpy as np
# concatenate 
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print("concatenate axis=0",np.concatenate((a,b),axis=0))
print("concatenate axis=1",np.concatenate((a,b),axis=1))
# staking 
print("v stack",np.vstack((a,b)))
print("h stack",np.hstack((a,b)))
print("d stack",np.dstack((a,b)))