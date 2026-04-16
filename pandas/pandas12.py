import pandas as pd

dates=pd.date_range(start="2024-01-01",end="2024-01-07",freq="D")
dates=pd.date_range(start="2024-01-01",end="2024-03-07",freq="ME")
dates=pd.date_range(start="2024-01-01",end="2026-01-07",freq="YE")

print(dates)



data1={
    "start_date":["2023-01-01","2023-06-01"],
    "end_date":["2024-01-01","2024-06-01"]
}

df=pd.DataFrame(data1)

df["start_date"]=pd.to_datetime(df["start_date"])
df["end_date"]=pd.to_datetime(df["end_date"])

df["tenure_days"]=(df["end_date"]-df["start_date"]).dt.days

print(df)
