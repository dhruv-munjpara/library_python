import numpy as np
import pandas as pd

data={
    "name":["alice","bob","charlie","david",None],
    "age":[25,None,30,None,None],
    "city":["new york","london",None,None,None]
}
df=pd.DataFrame(data)
print(df)

print("dropna row and any is nan:\n",df.dropna(axis=0,how='any'))
print("dropna row and all is nan:\n",df.dropna(axis=0,how='all'))
print("dropna coloumn and any is nan:\n",df.dropna(axis=1,how='any'))
print("dropna coloumn and all is nan:\n",df.dropna(axis=1,how='all'))


print("fill nan value with column mean:\n",df["age"].fillna(df["age"].mean()))
print("fill nan value with column median:\n",df["age"].fillna(df["age"].median()))


print("fill all const vale where nan:\n",df.fillna("sss"))
print("fill column to all const vale where nan:\n",df["age"].fillna("27"))


df["city"]=df["city"].fillna(df["city"].mode()[0])
print("fill in mode:\n",df)

df["city"]=df["city"].fillna("unknown")
print("fill unknown where none:\n",df)