import scipy.stats as stats
conversion_rates_A = [0.12, 0.15, 0.11, 0.14, 0.13, 0.16, 0.17, 0.10, 0.12, 0.14]
conversion_rates_B = [0.10, 0.09, 0.11, 0.08, 0.12, 0.09, 0.13, 0.11, 0.10, 0.12]
t_statistic, p_value = stats.ttest_ind(conversion_rates_A, conversion_rates_B)
alpha = 0.05

if p_value < alpha:
    conclusion = "Reject the null hypothesis. There is a significant difference."
else:
    conclusion = "Fail to reject the null hypothesis. There is no significant difference."
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)
print(conclusion)
