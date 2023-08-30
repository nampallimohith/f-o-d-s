import pandas as pd
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 30, 22, 35, 28, 30, 25, 22, 28, 35],
    'PurchaseAmount': [100, 150, 200, 120, 180, 250, 130, 110, 160, 140]
}
df = pd.DataFrame(data)
recent_month_df = df[df['PurchaseAmount'] > 0]  
age_distribution = recent_month_df['Age'].value_counts().sort_index() 
print("Age Frequency Distribution:")
print(age_distribution)
