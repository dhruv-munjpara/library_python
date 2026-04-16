import pandas as pd
df1=pd.DataFrame({"sales":[100,200]})
df2=pd.DataFrame({"sales":[300,400]})

print("merge:\n",pd.merge(df1,df2,how="outer",on="sales"))
print("concate:\n",pd.concat([df1,df2]))
print("concate:\n",pd.concat([df1,df2],ignore_index=True))

print("axis wise concate:\n",pd.concat([df1,df2],axis=1))