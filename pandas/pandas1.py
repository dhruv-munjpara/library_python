import pandas as pd
# series
# data=pd.Series([10,20,30,40])
# print(data)


# custom index in series
# data=pd.Series([10,20,30,40],index=["A","B","C","D"])
# print(data)
# print(data["A"])


data={
    "name":["rahul","prita","aman"],
    "age":[25,28,24],
    "salary":[50000,60000,70000]
}
print(type(data))
print(pd.DataFrame(data))
print(data)

