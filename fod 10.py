import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_values = [5000, 6000, 7500, 9000, 8000, 10000]

plt.plot(months, sales_values, marker='o', linestyle='-', color='b', label='Monthly Sales')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.legend()

plt.show()
