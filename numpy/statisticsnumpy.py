import numpy as np
data=np.array([10,20,30,40,50])
print("mean",np.mean(data))
print("median",np.median(data))
print("standard deviation",np.std(data))
print("varriance",np.var(data))
print("minimum",np.min(data))
print("maximum",np.max(data))
print("sum",np.sum(data))
print("cumulative sum",np.cumsum(data))
print("90 th persentile",np.percentile(data,90))
print("product",np.prod(data))


# percentile process
# a=[10,20,30,40,50]
# p/100(n-1)
# if p=90
# so 
# 90/100*(5-1)
# 0.90*4=3.6
# 40=3
# 0.6
# 4 th indec=50
# 3 index=40
# gap=10
# 1-*0.6=6
# 40+6=46


