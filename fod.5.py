import numpy as np
fuel_efficiency = np.array([65,55,85,78,99])
average_fuel_efficiency = np.mean(fuel_efficiency)
model1_efficiency = fuel_efficiency[0]
model3_efficiency = fuel_efficiency[2]
percentage_improvement = ((model3_efficiency - model1_efficiency) / model1_efficiency) * 100
print("Average Fuel Efficiency:", average_fuel_efficiency, "mpg")
print("Percentage Improvement:", percentage_improvement, "%")
