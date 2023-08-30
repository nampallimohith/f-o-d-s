import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr',]
temperature = [15, 18, 20, 22,]
plt.figure(figsize=(10, 6))
plt.plot(months, temperature, marker='o')
plt.title('Monthly Temperature Data')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
