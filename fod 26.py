from sklearn.linear_model import LinearRegression
dataset = [
    {"area": 1400, "bedrooms": 3, "location": "Suburb", "price": 250000},
    {"area": 1600, "bedrooms": 4, "location": "City", "price": 320000},
    {"area": 1200, "bedrooms": 2, "location": "Rural", "price": 180000},
    
]

X = [[house["area"], house["bedrooms"]] for house in dataset]
y = [house["price"] for house in dataset]
model = LinearRegression()
model.fit(X, y)
area = float(input("Enter the area of the house: "))
bedrooms = int(input("Enter the number of bedrooms: "))
new_house = [[area, bedrooms]]
predicted_price = model.predict(new_house)
print("Predicted price:", predicted_price[0])
