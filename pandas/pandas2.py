import pandas as pd
df=pd.read_csv("D:\DA&DS\pandas\california_housing_test.csv")
print(df)

# viweing data
# 1.head()->first 5 rows
print("first 5 rows:\n",df.head())
# 2.tail()->last 5 rows
print("last 5 rows:\n",df.tail())


# dataset summary information
print("info:\n",df.info())
print("describe:\n",df.describe())

# exporting data
# pandas also exporting dataset
# export to cvs=== df.to_cvs("output.cvs")
# export to excel=== df.to_excel("output.xscl")

print("convert to excel",df.to_excel("output.xlsx"))