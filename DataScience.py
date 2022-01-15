import pandas as pd
import matplotlib.pyplot as plt

def getAOV(column: list) -> int:
    res = 0
    size = len(column)

    for i in column:
        res += i
    res /= size
    return res


df = pd.read_csv('2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv')

# Are there are null elements
print("Are there any null elements: " + str(df.isnull().values.any()))

# Reproduce naive AOV
print("Naive average order value: " + str(getAOV(df['order_amount'])))

# Identify data point that stand out
df['total_items'].value_counts(ascending=True).sort_index().plot(kind='bar', rot=0, ylabel='count')
plt.show()

# Graph shows that there is some outlying orders with 2000 as the value of total items
print("New average order value: " + str(getAOV(df.query('total_items<6')['order_amount'])))


