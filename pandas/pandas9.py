import pandas as pd

# split()
# split strio=ng into multiple parts
data={
    "name":["aman sharma","priya patel","rahul verma"]
}
df=pd.DataFrame(data)
df["split_name"]=df["name"].str.split(" ")
print(df)