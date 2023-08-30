import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 15000, 11000, 13000, 14000,]

plt.figure(figsize=(10,6)) 
plt.bar(months, sales) 
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')

plt.grid(True)  
plt.show()
