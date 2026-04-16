import pandas as pd
# Question 1
# Create a DataFrame:
# Name = ["Aman Sharma", "Priya Patel", "Rahul Verma"]
# Tasks:
# • Convert all names to lowercase
# • Convert all names to uppercase

data={
    "name":["Aman Sharma", "Priya Patel", "Rahul Verma"]
}
df=pd.DataFrame(data)
# • Convert all names to lowercase
# df["name_lower"]=df["name"].str.lower()
# print(df)
# • Convert all names to uppercase
# df["name_upper"]=df["name"].str.upper()
# print(df)



# Question 2
# Using the same dataset:
# • Split names into first and last names
# df["split_name"]=df["name"].str.split(" ")
# print(df)
# • Store them in two separate columns
# df[["first_name,","last_name"]]=df["name"].str.split(" ",expand=True)
# print(df)

# or
# data={
#     "name":["Aman Sharma", "Priya Patel", "Rahul Verma"]
# }
# df=pd.DataFrame(data)
# df["f"]=df["name"].str.split(" ").str[0]
# df["l"]=df["name"].str.split(" ").str[1]
# print(df)


# Question 3
# Create a column:
# data1={"Category" : ["Electronics", "electronics", "ELECTRONICS", "Clothing"]}
# Tasks:
# df=pd.DataFrame(data1)
# • Normalize all values to lowercase
# df["lower"]=df["Category"].str.lower()
# print(df)
# • Count how many times "electronics" appears
# count = (df["lower"] == "electronics").sum()
# print(df)
# print("ele count",count)


# Question 4
# Create a column:
# data3={"Product" :["Phone-123", "Laptop-456", "Tablet-789"]}
# df=pd.DataFrame(data3)
# Tasks:
# • Remove numbers using str.replace()
# df["celan_name"]=df["Product"].str.replace(r"-\d+","",regex=True)
# print(df)
# • Keep only product names
# df["product_name"] = df["Product"].str.replace(r"[^A-Za-z]", "", regex=True)
# print(df)


# Question 5
# Create a column:
# Email = ["aman@gmail.com", "priya@yahoo.com", "rahul@gmail.com"]
# Tasks:
# • Filter only Gmail users using str.contains()
# data4 = {"Email": ["aman@gmail.com", "priya@yahoo.com", "rahul@gmail.com"]}
# df4 = pd.DataFrame(data4)
# filter gmail users
# gmail_users = df4[df4["Email"].str.contains("gmail")]
# print(gmail_users)


# Question 6
# Create a column:
# data={"text" : ["apple orange", "banana mango", "grape apple"]}
# df=pd.DataFrame(data)
# Tasks:
# • Check which rows contain the word "apple"
# contain_apple=df["text"].str.contains("apple")
# print(contain_apple)
# • Return only those rows
# print(df[contain_apple])


# Question 7
# Create a column:
# City = ["Delhi", "Mumbai", None, "Bangalore"]
# Tasks:
# • Replace missing values with "Unknown"
# • Convert all values to uppercase

# data={
# "City" : ["Delhi", "Mumbai", None, "Bangalore"]
# }
# df=pd.DataFrame(data)
# print(df["City"].fillna("unknow"))
# print(df["City"].str.upper())


# Question 8
# Create a column:
# Date = ["2024-01-01", "2024-02-15", "2024-03-10"]
# Tasks:
# • Convert the column to datetime
# • Extract year and month
# data={
# "Date" : ["2024-01-01", "2024-02-15", "2024-03-10"]
# }
# df=pd.DataFrame(data)
# df["Date"]=pd.to_datetime(df["Date"])
# df["day"]=df["Date"].dt.day
# df["month"]=df["Date"].dt.month
# df["year"]=df["Date"].dt.year
# print(df)


# Question 9
# Using the same dataset:
# • Extract only the day
# • Create a new column "Day_Name" (optional: weekday)
# data={
# "Date" : ["2024-01-01", "2024-02-15", "2024-03-10"]
# }
# df=pd.DataFrame(data)
# df["Date"]=pd.to_datetime(df["Date"])
# df["day"]=df["Date"].dt.day
# df["Day_name"]=df["Date"].dt.day_name()
# print(df)


# Question 10
# Create a date range from:
# Start = "2024-01-01"
# End = "2024-01-05"
# Tasks:
# • Generate dates using pd.date_range()
# • Convert it into a DataFrame

# dates=pd.date_range(start="2024-01-01",end="2024-01-05",freq="D")
# df=pd.DataFrame(dates,columns=["Date"])
# print(df)


# Question 11
# Create a dataset:
# Start_Date = ["2023-01-01", "2023-06-01"]
# End_Date = ["2024-01-01", "2024-06-01"]
# Tasks:
# • Convert both columns to datetime
# • Calculate tenure in days

# date={
# "Start_Date" : ["2023-01-01", "2023-06-01"],
# "End_Date" : ["2024-01-01", "2024-06-01"]
# }
# df=pd.DataFrame(date)
# print(df)
# df["Start_Date"]=pd.to_datetime(df["Start_Date"])
# df["End_Date"]=pd.to_datetime(df["End_Date"])

# df["Tenure_Days"]=(df["End_Date"]-df["Start_Date"]).dt.days
# print(df)

# Question 12
# Create a dataset:
# Date = ["2024-01-01", "invalid", "2024-03-10"]
# Tasks:
# • Convert to datetime using errors="coerce"
# • Identify invalid dates
# data={
# "Date" : ["2024-01-01", "invalid", "2024-03-10"]
# }
# df=pd.DataFrame(data)
# df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
# print(df)
# invalid_dates=df[df["Date"].isna()]
# print(invalid_dates)

# Question 13
# Create a dataset:
# Product = ["Mobile Phone", "Laptop", "Phone Case"]
# Tasks:
# • Filter rows where the word "Phone" exists
# • Ignore case sensitivity
# data={
# "Product" : ["Mobile Phone", "Laptop", "Phone Case"]
# }
# df=pd.DataFrame(data)
# result=df[df["Product"].str.contains("phone",case=False)]
# print(result)


# Question 14
# Create a dataset:
# Full_Name = ["Aman Sharma", "Priya Patel", "Rahul Verma"]
# Tasks:
# • Extract only last names
# • Create a new column "Last_Name"
# data={
# "Full_Name" : ["Aman Sharma", "Priya Patel", "Rahul Verma"]
# }
# df=pd.DataFrame(data)
# df["last_name"]=df["Full_Name"].str.split(" ").str[1]
# print(df)


# Question 15 — Data Cleaning + Time Analysis
# Create a dataset:
# Customer, Category, Start_Date, End_Date
# Include:
# • Mixed case category values
# • Missing values in Category
# • Date columns as strings
# Create dataset
data = {
    "Customer": ["Aman", "Priya", "Rahul", "Sneha"],
    "Category": ["Electronics", "electronics", None, "Clothing"],
    "Start_Date": ["2023-01-01", "2023-05-10", "2023-07-01", "2023-09-15"],
    "End_Date": ["2024-01-01", "2024-05-10", "2024-07-01", "2024-09-15"]
}

df = pd.DataFrame(data)
# Tasks:
# 1 Clean Category column
# • Convert to lowercase
df["Category"]=df["Category"].str.lower()
# • Replace missing values with "unknown"
df["Category"]=df["Category"].fillna("unknown")

# 2 Convert Start_Date and End_Date to datetime
df["Start_Date"]=pd.to_datetime(df["Start_Date"])
df["End_Date"]=pd.to_datetime(df["End_Date"])

# 3 Calculate tenure in days
df["Tenure_Days"]=(df["End_Date"]-df["Start_Date"]).dt.days

# 4 Extract Year and Month from Start_Date
df["Extract Year"]=df["Start_Date"].dt.year
df["Extract Month"]=df["Start_Date"].dt.month

# 5 Filter customers with tenure > 200 days
tenure_filter=df[df["Tenure_Days"]>200]
# 6 Identify rows where Category contains "electronics"
electronics_filter = df[df["Category"].str.contains("electronics", case=False)]

print(df)
print("\nTenure > 200:\n", tenure_filter)
print("\nElectronics:\n", electronics_filter)