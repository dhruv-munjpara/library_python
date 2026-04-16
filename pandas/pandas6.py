import pandas as pd
# session 6 
# handling dup;icate and outliers



# handling duplicate
data={
    "customer":["aman","priya","aman","rahul"],
    "sales":[500,700,500,900]
}

# df=pd.DataFrame(data)
# print(df)

# print(df.drop_duplicates())

# detecting outlier using iqr method
# iqr=interqurtile range
# formula
# iqr=q3-q1
# lowerbound=q1-1.5*iqr
# lowerbound=q1+1.5*iqr


sales=pd.Series([100,120,130,110,115,500])


Q1=sales.quantile(0.25)
Q3=sales.quantile(0.75)

IQR=Q3-Q1

lower=Q1-1.5*IQR
upper=Q3+1.5*IQR

outliers=sales[(sales<lower)|(sales>upper)]
print(outliers)


mean=sales.mean()
std=sales.std()

Z_scores=(sales-mean)/std
print(Z_scores)