import pandas as pd

cuatomers={
    "customer_id":[1,2,3],
    "name":["aman","priya","rahul"]
}
sales={
    "customer_id":[1,2,4],
    "amount":[500,700,300]
}

df=pd.DataFrame(cuatomers)
df1=pd.DataFrame(sales)

print(df)
print(df1)
inner_merge_data=pd.merge(df,df1,how="inner",on="customer_id")
print("inner join:\n",inner_merge_data)

left_merge_data=pd.merge(df,df1,how="left",on="customer_id")
print("left join:\n",left_merge_data)

right_merge_data=pd.merge(df,df1,how="right",on="customer_id")
print("right join:\n",right_merge_data)

outer_merge_data=pd.merge(df,df1,how="outer",on="customer_id")
print("outer join:\n",outer_merge_data)
