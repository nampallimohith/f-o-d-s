import matplotlib.pyplot as plt
import scipy.stats as stats

body_fat_percent_data = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

plt.figure(figsize=(8, 6))
stats.probplot(body_fat_percent_data, dist="norm", plot=plt)
plt.title("Q-Q Plot: %Fat")
plt.show()
