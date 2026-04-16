import pandas as pd
data = {
"Customer": ["Aman", "Priya", "Rahul", "Sneha", "Karan"],
"City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai"],
"Revenue": [12000, 8000, 15000, 7000, 20000]
}
df = pd.DataFrame(data)

# 1.Display the entire dataset
# print(df)

# 2
# Select only the Revenue column.
# print(df["Revenue"])

# 3
# Select the Customer and Revenue columns together
# print(df[["Customer","Revenue"]])


# 4
# Using loc, display the second row of the dataset.
# print(df.loc[1])

# 5   
# Using iloc, display the third row of the dataset.
# print(df.iloc[2])


# 6
# Using loc, retrieve the Revenue value of Rahul.
# print(df.loc[2,"Revenue"])

# 7
# Filter the dataset to show customers whose Revenue is greater than 10000
# print(df[df["Revenue"]>10000])

# 8
# Display customers who belong to Mumbai.
# print(df[df["City"]=="Mumbai"])