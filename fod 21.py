import numpy as np
import pandas as pd
from scipy.stats import norm
data = pd.read_csv('C:/Users/mohit/Downloads/_rare_element_.csv - Sheet1.csv')
measurements = data['concentration']
sample_size = int(input("Enter sample size: "))
confidence_level = float(input("Enter confidence level (between 0 and 1): "))
precision = float(input("Enter desired level of precision: "))


sample_mean = np.mean(measurements)
sample_std = np.std(measurements, ddof=1)  

z_score = norm.ppf(1 - (1 - confidence_level) / 2)
margin_of_error = z_score * (sample_std / np.sqrt(sample_size))


confidence_interval_lower = sample_mean - margin_of_error
confidence_interval_upper = sample_mean + margin_of_error

required_sample_size = ((z_score * sample_std) / precision) ** 2

print("\nPoint Estimation:")
print("Sample Mean:", sample_mean)
print("\nConfidence Interval:")
print("Lower:", confidence_interval_lower)
print("Upper:", confidence_interval_upper)
print("\nRequired Sample Size for Desired Precision:", required_sample_size)
