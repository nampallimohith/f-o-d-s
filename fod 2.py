
import numpy as np
sales_data = np.array([
    [100, 150, 200],
    [80, 120, 160],
    [120, 90, 110]
])

total_prices = np.sum(sales_data)
total_products = sales_data.shape[0]
average_price = total_prices / total_products

print("Average price of all products:", average_price)
