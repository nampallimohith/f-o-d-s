import pandas as pd

data = {
    'customer_id': [121,212, 361, 333, 222, 111],
    'order_date': ['2023-01-15', '2023-01-16', '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-18'],
    'product_name': ['rice', 'Bins', 'fruits', 'Caps', 'Ball', 'Dal'],
    'order_quantity': [2,3,1,4,2,1]
}

order_data = pd.DataFrame(data)

total_orders_per_customer = order_data.groupby('customer_id')['order_date'].count()

average_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print("Total Number of Orders by Customer:")
print(total_orders_per_customer)

print("\nAverage Order Quantity for Each Product:")
print(average_quantity_per_product)

print("\nEarliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
