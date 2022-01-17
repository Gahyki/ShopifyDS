## Q1  
### Setup
The first step is to be able to reproduce the naively calculated value.  
This is achieved by importing the csv as a dataframe then calculating the mean of the order_amount column.
![Naively calculated average code](/Question1/NaivelyCalculatedValueCode.png) 
![Naively calculated average](/Question1/NaivelyCalculatedValue.png)  
Then the data is verified for NaN/None values.  
Now the data is ready for further analysis.  
  
### 1A - Remove bulk orders
By quickly taking a look at the raw data, some data points seems to be off.  
So, I sort the dataframe by order_amount and total_items columns and was given the following result.  
![Sorted dataframe code](/Question1/BulkOrderCode.png)
![Sorted dataframe](/Question1/BulkOrder.png)  
It looks as if there was a bulk order that was done periodically by a certain user.  
Since the objective of the average order value (AOV) is to find the amount spent by an average user, these data points did not qualify to be computed as a part of the AOV.  
Therefore, the data points are excluded which resulted in this new average order value:  
![AOV after removing bulk orders code](/Question1/PostBulkAOVCode.png)  
![AOV after removing bulk orders](/Question1/PostBulkAOV.png)  
  
### 1A - Remove high price items
Once looking over the dataframe after the modification, there is another set of outlying data points.  
I could roughly deduce that it is items with high cost.  
To be sure, I extracted the various items' prices and to identify the outlier.  
![Item prices code](/Question1/ItemPricesCode.png)  
![Item prices](/Question1/ItemPrices.png)  
Just like my hypothesis, there is an item that has a drastically higher price point than the other items which has a value of 25725.  
![AOV without high price items code](/Question1/PostHighPriceAOVCode.png)  
![AOV without high price items](/Question1/PostHighPriceAOV.png)  
If there are a large number of orders for the high price item, it might actually be reasonable to keep the item as a part of the average.  
So to verify this, its contribution to the average is calculated in percentage.  
![High price item contribution in percentage code](/Question1/HighPriceContributionCode.png)  
![High price item contribution in percentage](/Question1/HighPriceContribution.png)  
It resulted in less than 1%, thus it is concluded that this set of data points can be neglected for the purpose of finding the optimal AOV.  

### 1B - What metric would you report for this dataset?
There are various metrics that can be extracted from this dataset.  
One potentially interesting metric could be the contribution of high price items that was calculated.  
The set of data points generates enough revenue to be able to double the average order value if it was considered.  
Another metric that could be extracted from this dataset is the most popular items based on order frequency.  

### 1C - What is its values?
Here is a side by side comparison of the AOV with and without the high price items:  
![AOV with high price items](/Question1/PostBulkAOV.png)  
![AOV without high price items](/Question1/PostHighPriceAOV.png)  
  
The following is the list of top ten most popular items in order of frequency:  
![Popularity by order frequency code](/Question1/PopularityByOrderFrequencyCode.png)
![Popularity by order frequency](/Question1/PopularityByOrderFrequency.png)  
  
and a graphical representation of the popularity of each item price (by order of frequency):
![Popularity graph code](/Question1/PopularityGraphCode.png)  
![Popularity graph](/Question1/PopularityGraph.png)  
