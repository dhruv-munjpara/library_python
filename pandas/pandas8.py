import pandas as pd

data={
    "category":["Electronics","electronics","ELECTRONICS","clothing"]
}

df=pd.DataFrame(data)


df["category_lower"]=df["category"].str.lower()
df["category_upper"]=df["category"].str.upper()

print(df)

df["category_clean"]=df["category"].str.replace("Electronics","Electronics Items")
print(df)


# contains()
# check if substring exists in each element
df[df["category"].str.contains("Electronics",case=False)]


