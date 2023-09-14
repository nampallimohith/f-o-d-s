import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
data = pd.read_csv('C:/Users/mohit/Downloads/transaction_data_csv - Sheet1.csv')  
selected_features = data[['total_amount_spent', 'visit_frequency']]
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(selected_features)
    sse.append(kmeans.inertia_)

plt.figure()
plt.plot(range(1, 11), sse, marker='o')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('SSE')
plt.title('Elbow Method')
plt.show()

num_clusters = 4  
kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
cluster_assignments = kmeans_model.fit_predict(selected_features)
cluster_centers = kmeans_model.cluster_centers_
data['cluster'] = cluster_assignments
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(selected_features)
plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=cluster_assignments, cmap='viridis')
plt.xlabel('PCA Component 1')
