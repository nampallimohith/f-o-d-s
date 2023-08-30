from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
dataset = [
    {"usage_minutes": 500, "contract_duration": 12, "churn": 0},
    {"usage_minutes": 300, "contract_duration": 6, "churn": 1},
    {"usage_minutes": 800, "contract_duration": 24, "churn": 0},
    
]

X = [[customer["usage_minutes"], customer["contract_duration"]] for customer in dataset]
y = [customer["churn"] for customer in dataset]
model = LogisticRegression()
model.fit(X, y)
usage_minutes = float(input("Enter the usage minutes: "))
contract_duration = int(input("Enter the contract duration: "))
new_customer = [[usage_minutes, contract_duration]]
predicted_churn = model.predict(new_customer)

if predicted_churn[0] == 0:
    print("Predicted: Not Churn")
else:
    print("Predicted: Churn")
