import pandas as pd
data = {
    'product_name': ['A', 'B', 'A', 'C', 'E', 'D', 'D', 'C', 'E', 'A'],
    'quantity_sold': [10, 15, 8, 20, 12, 6, 5, 18, 9, 11]
}
sales_data = pd.DataFrame(data)
product_sales = sales_data.groupby('product_name')['quantity_sold'].sum()
top_products = product_sales.sort_values(ascending=False).head(5)
print("Top 5 Products Sold:")
print(top_products)
