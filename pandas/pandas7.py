# column operation and data tranformation
import pandas as pd
data={
    "product":["pen","notebook","marker"],
    "price":[10,50,20],
    "qty":[100,40,60]
}

df=pd.DataFrame(data)
print(df)

df["revenue"]=df["price"]*df["qty"]
print(df)

df["price_with_tax"]=df["price"].apply(lambda x:x*1.18)
print(df)

df_numeric=df[["price","qty"]]
print(df_numeric.map(lambda x:x*2))

