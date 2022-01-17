## Q2  
In depth explanation of my queries are in Question2/q2.txt  
a) How many orders were shipped by Speedy Express in total?  
![a answer](/Question2/a.png)  
In a large dataset, it is not realistic to find the ID of the shipper directly, so the query above is required.  
However, the following would be more efficient for this dataset:  
  
SELECT count(ShipperID) FROM Orders  
WHERE ShipperID = 1;  
  
b) What is the last name of the employee with the most orders?  
![b answer](/Question2/b.png)  
M number of orders joined with N number of Employees can become a very large table.  
For an increase in performance in larger datasets, the employee with the most orders is found first before finding their last name.  
  
c) What product was ordered the most by customers in Germany?  
![c answer](/Question2/c.png)
