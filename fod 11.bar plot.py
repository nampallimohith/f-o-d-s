import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [1000, 700, 900, 1100, 1200]
plt.figure(figsize=(10, 6))
plt.bar(months, sales, color='green')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
