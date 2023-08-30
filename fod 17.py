import pandas as pd
import numpy as np



age_data = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 56, 57, 58, 58, 60, 61]
body_fat_percent_data = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
  
df = pd.DataFrame({'Age': age_data, 'BodyFatPercent': body_fat_percent_data})

mean_age = df['Age'].mean()
median_age = df['Age'].median()
std_dev_age = df['Age'].std()

mean_body_fat_percent = df['BodyFatPercent'].mean()
median_body_fat_percent = df['BodyFatPercent'].median()
std_dev_body_fat_percent = df['BodyFatPercent'].std()

print("Age:")
print(f"Mean: {mean_age:.2f}")
print(f"Median: {median_age}")
print(f"Standard Deviation: {std_dev_age:.2f}\n")

print("Body Fat Percentage:")
print(f"Mean: {mean_body_fat_percent:.2f}")
print(f"Median: {median_body_fat_percent}")
print(f"Standard Deviation: {std_dev_body_fat_percent:.2f}\n")


