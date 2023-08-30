import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug' ]
rainfall = [50, 40, 60, 80, 100, 120, 150, 140,]

plt.figure(figsize=(10, 6))
plt.scatter(months, rainfall, color='red', marker='o')
plt.title('Monthly Rainfall Data')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()
