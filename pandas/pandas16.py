import pandas as pd

data={
    "month":["jan","jan","feb","feb"],
    "product":["A","B","A","B"],
    "sales":[100,200,150,250]
}

df=pd.DataFrame(data)
print(df.pivot(index="month",columns="product",values="sales"))

# important rule(very important)
# pivot works only when:
# each(index,column) pair has one values
# if duplicates exist-->error
