import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 1, 0, 1])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
new_patient_features = []
for i in range(X.shape[1]):
    feature_value = float(input(f"Enter value for feature {i+1}: "))
    new_patient_features.append(feature_value)
new_patient_features = np.array(new_patient_features).reshape(1, -1)
k = int(input("Enter the value of k: "))
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X_train_scaled, y_train)
new_patient_features_scaled = scaler.transform(new_patient_features)
prediction = knn_classifier.predict(new_patient_features_scaled)
if prediction[0] == 0:
    print("Prediction: No medical condition.")
else:
    print("Prediction: Medical condition present.")
