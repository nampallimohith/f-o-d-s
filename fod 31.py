import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data = pd.read_csv('C:/Users/mohit/Downloads/customer_data_csv - Sheet1.csv')
selected_features = ['purchase_history', 'browsing_behavior', 'demographics']
X = data[selected_features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
num_clusters = 4
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
data['cluster'] = clusters
plt.scatter(data['purchase_history'], data['browsing_behavior'], c=data['cluster'], cmap='rainbow')
plt.xlabel('Purchase History')
plt.ylabel('Browsing Behavior')
plt.title('Customer Segmentation')
plt.show()
