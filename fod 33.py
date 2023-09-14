import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
data = pd.read_csv('C:/Users/mohit/Downloads/car_data_33-csv - Sheet1.csv') 
selected_features = ['engine_size', 'horsepower', 'fuel_efficiency', 'age']
target = 'price'
X = data[selected_features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
coefficients = model.coef_
intercept = model.intercept_
print("Coefficients:")
for feature, coefficient in zip(selected_features, coefficients):
    print(f"{feature}: {coefficient:.2f}")
print(f"Intercept: {intercept:.2f}")
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual Prices vs Predicted Prices')
plt.show()
