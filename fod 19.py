import scipy.stats as stats
n1 = 25
x_bar1 = 2.3  
s1 = 1.2      

n2 = 25
x_bar2 = 1.5  
s2 = 1.0

critical_value = stats.norm.ppf(0.975)  
ci_drug = (x_bar1 - critical_value * (s1 / (n1**0.5)), x_bar1 + critical_value * (s1 / (n1**0.5)))
ci_placebo = (x_bar2 - critical_value * (s2 / (n2**0.5)), x_bar2 + critical_value * (s2 / (n2**0.5)))

print("95% Confidence Interval for Drug Group:", ci_drug)
print("95% Confidence Interval for Placebo Group:", ci_placebo)
