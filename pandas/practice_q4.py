import pandas as pd
# q1
# df1=pd.DataFrame({"id":[1,2,3],
#                   "name":["aman","priya","rahul"]
#                 })

# df2=pd.DataFrame({"id":[2,3,4],
#                   "score":[80,90,70] })

# perform merge without sqecify how
# merge1=pd.merge(df1,df2,on="id")
# print(merge1)
# explain which rows will appear and why
# how many rows will be in output


# q2-duplicate key explosion
# df1=pd.DataFrame({"id":[1,1],
#                   "product":["A","B"]})

# df2=pd.DataFrame({"id":[1,1],
#                   "price":[100,200]})

# task:
# 1.perform inner merge
# inner_mearge=pd.merge(df1,df2,how="inner",on="id")
# print(inner_mearge)
# 2.count number of rows in output
# 3.explian why rows increase(hint:cartesian multiplication)


# 3.left join with missing values
# df1=pd.DataFrame({"id":[1,2,3],
#                   "name":["aman","priya","rahul"]})

# df2=pd.DataFrame({"id":[1],
#                   "salary":[50000]})
# task:
# 1.perform left join
# left_join=pd.merge(df1,df2,how="left",on="id")
# print(left_join)
# 2.identify rows with missing salary
# missing=left_join[left_join["salary"].isna()]
# print(missing)
# 3.fill missing salary with 0
# left_join["salary"]=left_join["salary"].fillna(0)
# print(left_join)


# q4-multiple key merge trap
# df1=pd.DataFrame({"id":[1,1],
#                   "city":["delhi","mumbai"],
#                   "sales":[100,200]})

# df2=pd.DataFrame({"id":[1],
#                   "city":["delhi"],
#                   "target":[150]})

# task:
# 1.merge using only id
# id_merge=pd.merge(df1,df2,on="id")
# print(id_merge)
# 2.merge using id+city
# id_city_merge=pd.merge(df1,df2,on=["id","city"])
# print(id_city_merge)
#3.compare both output
# explain why result is diffrent


# q.5-real-world mearge scenario
# create:
df1=pd.DataFrame({"customer_id":[1,2,3,],
                  "name":["aman","priya","rahul"]})

df2=pd.DataFrame({"customer_id":[1,1,2],
                  "order_amount":[500,700,300]})

# task:
# 1.merge both dataset
both_merge=pd.merge(df1,df2,on="customer_id")
# print(both_merge)
# 2.calculate total order amount per customer
total_order=both_merge.groupby(["customer_id","name"])["order_amount"].sum().reset_index()
print(total_order)
# 3.identify customer with no orders
# left_join=pd.merge(df1,df2,how="left",on="customer_id")
# print(left_join)
# no_orders=left_join[left_join["order_amount"].isna()]
# print(no_orders)
# 4.replase missing values with 0
# left_join["order_amount"]=left_join["order_amount"].fillna(0)
# print(left_join)