import pandas as pd
data={
    "customer":["aman","priya","rahul","sneha","karan"],
    "city":["delhi","munbai","delhi","banglore","mumbai"],
    "revenue":[12000,8000,15000,7000,20000]
}

df=pd.DataFrame(data)
# print(df)
# print(df["revenue"])
# print(df[["customer","revenue","city"]])

# select first row
# print("first row:\n",df.loc[0])
# select specific valu
# print("specific val:",df.loc[2,"revenue"])


# # iloc 
# print(df.iloc[2])
# print(df.iloc[2,2])

# bolean filtering
# print(df["revenue"]>10000)
# print(df[df["revenue"]>10000])

# logical
# print((df["revenue"]>10000)&(df["city"]=="delhi"))
# print(df[(df["revenue"]>10000)&(df["city"]=="delhi")])

# query function same as bollean logical condition
# print(df.query("revenue>10000"))

# print("high revenue customer:\n",df[df["revenue"]>10000])



# sorting and reindexing
# print("original val:\n",df)
# print("by revenue:\n",df.sort_values(by="revenue"))
# print("by city:\n",df.sort_values(by="city"))
# print("by customer:\n",df.sort_values(by="customer"))

# # decending
# print("by revenue decending:\n",df.sort_values(by="revenue",ascending=False))


# soring multiple column
# print("sorting munliple column",df.sort_values(by=["city","revenue"]))




# reset index
# sorted_index=df.sort_values(by="revenue")
# print(sorted_index.reset_index())
# print(sorted_index.reset_index(drop=True))