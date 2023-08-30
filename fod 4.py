import numpy as np
sales_data = np.array([100000, 150000, 120000, 180000])
total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print("Total Sales for the Year:", total_sales)
print("Percentage Increase in Sales:", percentage_increase, "%")
