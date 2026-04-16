import numpy as np
# session 9:: mini case study
# objective of this session
# in this session we will connect everything learned in previous
#  session and applay it to small real world dataset
# so far we have learned
# 1.array creation
# 2.mathemetical operation
# 3.stastical function
# 4.indexing and slicing
# 5.array manipulation
# 6.utility function
# 7.handloing missing values
# m=now we will apply these concept to a simple dataset
#===================================


# case study::store salse dataet
# assume we have data from a small store
# each prodct has:
    # 1.price]
    # 2.Quantity sold

# from this dataset we want to compute:
# total revenue
# average price
# product with highest salse
# clean missing values
# Generate summary statistics
# this is similar to real data preprocessing task in data science

# step::1
# we create teo array
# price of product
# Quantity sold

price=np.array([100,200,150,300,np.nan,250])
quantity=np.array([10,5,8,3,7,6])
print("price:",price)
print("Quantity:",quantity)


# step::2--data cealning
# real-world dataset often contain missing values.
# in our dataset one price value is missing(NaN)
# we will
    # 1.identity misiing values
    # 2.replace missing values with average price

# detect missing values
print("missing values in price:",np.isnan(price))
# claculate average price ingnoring NaN
avg_price=np.nanmean(price)
print("average price",avg_price)
# replce NaN with average price
price=np.where(np.isnan(price), avg_price,price)
print("celan price:",price)
 

# step::3--perform arithmetic operation
# revenue=price*quantity
# this uses element wise multiplication
revenue_price=price*quantity
print("revenue for each product:",revenue_price)


# step::4--generate summary statistics
# now we compute statistics:
#     1.total revenue_price
#     2.average_revenue
#     3.max_revenue
#     4.min_revenue

print("total revenue:",np.sum(revenue_price))
print("average revenue:",np.mean(revenue_price))
print("maximum revenue:",np.max(revenue_price))
print("minimum revenue:",np.min(revenue_price))


# step::5--indentify best selling product
# we want to find which product generated the higjest revenue.
# for this we use
# np.argmax()
# this return the index of the maximun value.

best_product_index=np.argmax(revenue_price)
print("best selling product index:",best_product_index)
print("revenue generated:",revenue_price[best_product_index])


# step::6--sorting products by revenue
# sorting  help us rank product
# we sue: np.argsort()
sorted_indices=np.argsort(revenue_price)
print("sorted product indices:",sorted_indices)
print("revenue sorted:",revenue_price[sorted_indices])


# step::7--identify high revenue products
# let us find products generating revenue grater than 1000
# we will use bollean indexing
 
high_revenue_product=np.where(revenue_price>1000)
print("indices with revenue>1000",high_revenue_product)
print("revenue values",revenue_price[high_revenue_product])



# step::8--final dataset summary
# now we crate a small summary of the dataset
# metrics:
    # 1.number of products
    # 2.total salse revenue
    # 3.average price
    # 4.average quantity

print("number of product",price.size)
print("total revenue",np.sum(revenue_price))
print("average price:",np.mean(price))
print("average quantity sold:",np.mean(quantity))