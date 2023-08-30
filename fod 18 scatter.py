import matplotlib.pyplot as plt

age_data = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 56, 57, 58, 58, 60, 61]
body_fat_percent_data = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

plt.figure(figsize=(8, 6))
plt.scatter(age_data, body_fat_percent_data)
plt.title("Scatter Plot: Age vs %Fat")
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.show()
