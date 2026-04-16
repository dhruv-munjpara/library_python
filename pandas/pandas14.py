import pandas as pd

df1=pd.DataFrame({"id":[1,1,2],
                  "city":["delhi","mumbai","delhi"],
                  "sales":[100,200,300]
                })


df2=pd.DataFrame({"id":[1,2],
                  "city":["delhi","delhi"],
                  "target":[150,350]
                })

inner_merge_data=pd.merge(df1,df2,on=["id","city"])#its defalt take inner 
print("inner join:\n",inner_merge_data)

