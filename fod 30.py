import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, export_text
data = pd.read_csv('C:/Users/mohit/Downloads/car_dataset_csv - Sheet1.csv')  

features = ['mileage', 'age', 'brand', 'engine_type']
target = 'price'

X = data[features]
y = data[target]

X = pd.get_dummies(X, columns=['brand', 'engine_type'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)
new_car_mileage = float(input("Enter the mileage of the new car: "))
new_car_age = float(input("Enter the age of the new car: "))
new_car_brand = input("Enter the brand of the new car: ")
new_car_engine_type = input("Enter the engine type of the new car: ")
new_car_data = pd.DataFrame({
    'mileage': [new_car_mileage],
    'age': [new_car_age],
    'brand_' + new_car_brand: [1], 
    'engine_type_' + new_car_engine_type: [1] 
})

predicted_price = regressor.predict(new_car_data)[0]
print(f"Predicted price for the new car: ${predicted_price:.2f}")

decision_path = regressor.decision_path(new_car_data)
tree_rules = export_text(regressor, feature_names=new_car_data.columns.tolist())
print("Decision path:")
print(tree_rules)
