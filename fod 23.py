import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


np.random.seed(42)
control_group = np.random.normal(3, 5,15)  
treatment_group = np.random.normal(15, 5, 5)
t_statistic, p_value = ttest_ind(control_group, treatment_group)
plt.figure(figsize=(8, 6))
plt.hist(control_group, bins=15, alpha=0.5, label='Control Group')
plt.hist(treatment_group, bins=15, alpha=0.5, label='Treatment Group')
plt.axvline(control_group.mean(), color='blue', linestyle='dashed', linewidth=2, label='Control Mean')
plt.axvline(treatment_group.mean(), color='orange', linestyle='dashed', linewidth=2, label='Treatment Mean')
plt.xlabel('Effectiveness')
plt.ylabel('Frequency')
plt.title('Effectiveness of Treatment vs. Placebo')
plt.legend()
plt.annotate(f'p-value = {p_value:.4f}', xy=(0.5, 0.85), xycoords='axes fraction', fontsize=12)
plt.show()
alpha = 0.05 
if p_value < alpha:
    print("Reject the null hypothesis. The new treatment has a statistically significant effect.")
else:
    print("Fail to reject the null hypothesis. The new treatment does not have a statistically significant effect.")
