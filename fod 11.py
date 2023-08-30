import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', ]
sales = [1000, 1200, 1250, 1100, ]
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o')
plt.title('Monthly Sales Prediction')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
