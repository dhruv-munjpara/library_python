import pandas as pd

data={
    "name":["dhruv munjpara","RAM chaudhary","KUMARPAL RATHOD","RAHUL patel","krishna ZALA"]
}

df=pd.DataFrame(data)

df["name_upper"]=df["name"].str.upper()
df["name_lower"]=df["name"].str.lower()
df["clean_name"]=df["name"].str.replace("dhruv munjpara","dhruv patel")
df[df["name"].str.contains("chaudhary",case=False)]
df["split_name"]=df["name"].str.split(" ")
print(df)
