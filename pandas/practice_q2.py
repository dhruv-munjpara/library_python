import pandas as pd
# q1. create a dataframe with columns:
# name,age,city,salary
data={
    "name":["dhruv","miten","het","ashok","tarang",None,"dhruv"],
    "age":[22,None,24,25,None,None,22],
    "city":["limbdi","mumbai","ahemdabad","delhi",None,None,"limbdi"],
    "salary":[45000,30000,52000,None,23500,None,45000]
}
df=pd.DataFrame(data)
# print(df)

# task
# >display only the age column
# print("age column:\n",df["age"])

# >display name and salary together
# print("name and salary column:\n",df[["name","salary"]])


# q2.using the same dataset:
# >select the 3rd row using iloc
# print("3rd row using iloc:\n",df.iloc[2])

# >select the salary of the 2nd row using loc
# print("salary of the 2nd row using loc:\n",df.loc[1,"salary"])

# q3.filter the dataset:
# >show rows where salary>50000
# print("rows where salary>50000:\n",df[df["salary"]>50000])
# >show rows where city is "delhi"
# print("rows where city is delhi:\n",df[df["city"]=="delhi"])


# q4.apply multiple conditions:
# >  salary>40000 and city="mumbai"
# print("salary>40000 and city=mumbai:\n",df[(df["salary"]>40000) & (df["city"]=="mumbai")])


# q5.sort the dataset:
# >sort by salary in ascending order
# print("sort by salary in ascending order:\n",df.sort_values(by="salary"))

# >sort by salary in descending order
# print("sort by salary in descending order:\n",df.sort_values(by="salary",ascending=False))

# q6.after sorting:
# >reset the index
# print("reset the index:\n",df.reset_index())

# >remove the old index
# print("remove the old index:\n",df.reset_index(drop=True))

# q7.create a dataset with missing values in age
# task:
# >detect misiing values using isnull()
# print("detect misiing values using isnull():\n",df.isnull())

# >count misiing values per column
# print("count misiing values using isnull().sum():\n",df.isnull().sum())

# q8.using the same dataset:
# >drop rows with missing values
# print("drop all rows with missing values:\n",df.dropna(axis=0,how='all'))
# print("drop any rows with missing values:\n",df.dropna(axis=0,how='any'))

# >drop column with missing values
# print("drop all column with missing values:\n",df.dropna(axis=1,how='all'))
# print("drop any column with missing values:\n",df.dropna(axis=1,how='any'))

# q9.fill missing values:
# >replace missing age with mean
# print("replace missing age with mean:\n",df["age"].fillna(df["age"].mean()))
# >replace missing city with "unknown"
# print("replace missing city with unknown:\n",df["city"].fillna("unknow"))

# q10.create a dataset with duplicate rows
# task:
# >identify duplicates
# print("identify duplicates:\n",df.duplicated())

# >remove duplicates rows
# print("remove duplicates rows:\n",df.drop_duplicates())


# q11. create a sales column
sales=pd.Series([100,120,110,115,500])
# print(sales)
# task
# >detect outliers using iqr method
# q1=sales.quantile(0.25)
# q3=sales.quantile(0.75)

# iqr=q3-q1

# lower=q1-1.5*iqr
# upper=q3+1.5*iqr

# outliers=sales[(sales<lower)|(sales>upper)]
# print(outliers)


# q12. using the same data 
# >calculate Z-score for each value
mean=sales.mean()
std=sales.std()
z_score=(sales-mean)/std
# print(z_score)

# >identify values where z_score>2
# print("identify values where z_score>2:\n",sales[z_score>2])


# q13.create dataset
data1={
    "product":["laptop","mobile","tablet","keyboard","mouse"],
    "price":[50000,20000,15000,800,500],
    "quantity":[5,10,7,20,25]
}
df1=pd.DataFrame(data1)
print(df1)

# >task:    
# >create new column revenue=price*quantity
# df1["revenue"]=df1["price"]*df1["quantity"]
# print(df1)
# >calculate total revenue
# print("calculate total revenue:\n",df1["revenue"].sum())


# q14.use apply() and lambda:
# >increase all prices by 10%
# df1["increase_price"]=df1["price"].apply(lambda x:x+x*0.10)
# >create a new column discountes price=price-10%
# df1["disconted_price"]=df1["price"].apply(lambda x:x-x*0.10)

# print(df1)



# final integrated question:
# q15.mini data celaning & analysis task

# create a dataset 
# customer,age,city,price,quantity
# missing values in age and city
# duplicated rows


data3={
    "customer":["dhruv","miten","het","ashok","tarang","dhruv"],
    "age":[22,24,None,25,None,22],
    "city":["limbdi","mumbai","ahmedabad","delhi",None,"limbdi"],
    "price":[500,1200,800,1500,700,500],
    "quantity":[2,1,3,1,4,2]
}

df3=pd.DataFrame(data3)
print(df3)

# tasks:

# 1 celaing missing values:
#>replace age with mean
print("replace age with mean:\n",df3["age"].fillna(df3["age"].mean()))
# >replace city with "unknow"
print("replace city with unknow:\n",df3["city"].fillna("unknow"))


# 2.remove duplicated rows
print("detect duplicated rows",df3.duplicated())
print("remove duplicated rows",df3.drop_duplicates())


# 3.create new column:
# revenue=price*quantity
df3["revenue"]=df3["price"]*df3["quantity"]
print(df3)

# 4. filter rows where revenue>500
print("filter rows where revenue>500:\n",df3["revenue"]>500)

# 5.sort the dataset by revenue in descending order
print("sort datset in decending order",df3.sort_values("revenue",ascending=False))

# 6.reset the index
print("reset index:\n",df.reset_index(drop=True))

# 7.indentify any outliers in revenue using iqr
q1=df3["revenue"].quantile(0.25)
q3=df3["revenue"].quantile(0.75)

iqr=q3-q1

lower=q1-1.5*iqr
upper=q3+1.5*iqr

outliers=df3[(df3["revenue"]<lower)|(df3["revenue"]>upper)]
print("outliers in revenue:\n",outliers)