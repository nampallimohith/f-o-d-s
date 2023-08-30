 from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

dataset = [
    {"total_spent": 100, "items_purchased": 5},
    {"total_spent": 200, "items_purchased": 10},
    {"total_spent": 50, "items_purchased": 3},
    
]
X = [[customer["total_spent"], customer["items_purchased"]] for customer in dataset]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
num_clusters = 3  
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X_scaled)
total_spent = float(input("Enter the total amount spent: "))
items_purchased = int(input("Enter the number of items purchased: "))
new_customer = [[total_spent, items_purchased]]
new_customer_scaled = scaler.transform(new_customer)
predicted_cluster = kmeans.predict(new_customer_scaled)

print("Predicted cluster:", predicted_cluster[0])
