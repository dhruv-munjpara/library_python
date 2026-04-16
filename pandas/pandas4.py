import pandas as pd
import numpy as np

data={
    "customer":["aman","priya","rahul","sneha"],
    "age":[25,np.nan,30,np.nan],
    "city":["delhi","mumbai","delhi","banglore"]
}
df=pd.DataFrame(data)
print("dataframe:\n",df)
print("true when is nan:\n",df.isnull())
print("column wise count where is nan:\n",df.isnull().sum())
print("drop nan val:\n",df.dropna())
print("dropna row and any is nan:\n",df.dropna(axis=0,how='any'))
print("dropna row and all is nan:\n",df.dropna(axis=0,how='all'))
