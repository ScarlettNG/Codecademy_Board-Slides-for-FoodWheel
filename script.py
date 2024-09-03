import codecademylib3

# 1
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt 
# Create restaurants dataframe
restaurants = pd.read_csv("restaurants.csv")
print(restaurants.head(10))
# Inspect restaurant dataframe

# Check number of unique cuisines
print(restaurants.cuisine.nunique())
# Group count by cuisine
cuisine_counts = restaurants.groupby("cuisine").id.count()
print(cuisine_counts)
# Inspect cuisine_counts dataframe

# Create a pie chart
plt.axis("equal")
plt.pie(cuisine_counts.values, labels = cuisine_counts.axes[0], autopct="%d%%")
plt.show()

# 2
# Create orders dataframe
orders = pd.read_csv("orders.csv")
print(orders.head(5))

# Inspect the orders dataframe
orders['month'] = orders['date'].apply(lambda date: date.split('-')[0])

# Create new month column

# Inspect new orders dataframe
no_orders = orders.groupby("month").id.count()
print(no_orders)

# Create average order by month dataframe
avg_order = orders.groupby("month").price.mean()
# Inspect avg_order dataframe
print(avg_order)

# Create standard deviation dataframe
std_order = orders.groupby("month").price.std()
# Inspect std_order
print(std_order)
# Create barplot
avg_order.index = avg_order.index.astype(int)
std_order.index = std_order.index.astype(int)
plt.close("all")
plt.bar(avg_order.index, avg_order.values, yerr=std_order.values, capsize =5)
plt.ylabel("Average Order Amount")
plt.title("Average Order Amount per Month with STD")
plt.show()

# 3
# Create customer amount dataframe
customer_amount = orders.groupby("customer_id").price.sum()
# Inspect customer amount
plt.close("all")
# Create histogram
plt.hist(customer_amount, range=(0, 200), bins = 40)
plt.xlabel("Total Spent")
plt.ylabel("Number of Customers")
plt.title("Distribution of Total Amount Spent by Customers")
plt.show()
