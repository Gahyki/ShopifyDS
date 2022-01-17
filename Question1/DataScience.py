import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)
df = pd.read_csv('2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv')

# Reproduce naive AOV
print("Naive average order value: " + str(df['order_amount'].mean()))

# Are there are null elements
print("Are there any null elements: " + str(df.isnull().values.any()))

# Identify data points that stand out
sorted_df = df.sort_values(by=['order_amount', 'total_items'], ascending=False)
print(sorted_df.head(25))

'''
-------------------------------- Remove bulk order data points ----------------------------------
The table shows that there are some outlying orders with 2000 total items.
These data points stand out because the other orders' total items are all in the single digits.
'''
# Only removed the bulk orders, meaning that high price items are still included in this new number
sorted_df = sorted_df.query('total_items != 2000')
print("New average order value: " + str(sorted_df['order_amount'].mean()))

'''
------------------------------ Remove price price item data points --------------------------------
To get the best average order value, it is important to exclude the high price items.
'''
# Identify high price items -> formula for price of item is order_amount/total_items
sorted_df['item_price'] = sorted_df['order_amount']/sorted_df['total_items']
print(np.unique(sorted_df.item_price))

'''
From this array, it possible to identify that the item with the value of 25725 is a significant
outlier, therefore this item shall be removed from the AOV
'''
cleaned_df = sorted_df.query('item_price < 25725')
print("New average order value: " + str(cleaned_df['order_amount'].mean()))

'''
----------------------------- Contribution of high price items -----------------------------------
If there are a large number of orders for the high price item, it might be reasonable to keep
the item as a part of the average. To verify this, its contribution will be calculated.
'''
# Find contribution of high price items
total_orders = len(sorted_df)
high_price_contribution = (1 - len(cleaned_df)/total_orders) * 100
print("High price item contribution percentage: " + str(high_price_contribution) + "%")
# Conclusion: Its contribution is less than 1 percent, therefore can be omitted

'''
---------------------------------- Find most popular items --------------------------------------
An interesting metric that could be extracted from this dataset is a list of the most 
popular items. This will allow one to be able to identify which shop and product is the most
well performing.
'''
cleaned_df.loc[:, 'item_price'].value_counts().head(10)

print(cleaned_df.loc[:, 'item_price'].value_counts().head(10))
print("The most popular item has the price of " +
      str(cleaned_df.loc[:, 'item_price'].value_counts().head(1).index[0]) +
      " and has sold a total of " +
      str(cleaned_df.loc[:, 'item_price'].value_counts().iloc[0]) +
      " units.")
