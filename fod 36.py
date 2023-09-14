import pandas as pd
import numpy as np
def read_stock_data(filename):
    df = pd.read_csv(filename)
    return df
def calculate_price_variability(closing_prices):
    mean_price = np.mean(closing_prices)
    price_variance = np.var(closing_prices)
    price_std_dev = np.std(closing_prices)
    return mean_price, price_variance, price_std_dev

def analyze_price_movements(closing_prices):
    price_changes = np.diff(closing_prices)
    positive_changes = price_changes[price_changes > 0]
    negative_changes = price_changes[price_changes < 0]
    
    num_positive_changes = len(positive_changes)
    num_negative_changes = len(negative_changes)
    total_changes = num_positive_changes + num_negative_changes
    
    avg_positive_change = np.mean(positive_changes)
    avg_negative_change = np.mean(negative_changes)
    
    return num_positive_changes, num_negative_changes, total_changes, avg_positive_change, avg_negative_change

if __name__ == "__main__":
    
    csv_filename = "C:/Users/mohit/Downloads/stock_data_csv - Sheet1.csv"
    
    stock_data = read_stock_data(csv_filename)
    
    closing_prices = stock_data["Closing Price"]  
    
    mean_price, price_variance, price_std_dev = calculate_price_variability(closing_prices)
    
    num_positive_changes, num_negative_changes, total_changes, avg_positive_change, avg_negative_change = analyze_price_movements(closing_prices)
    
    print("Price Variability:")
    print("Mean Price:", mean_price)
    print("Price Variance:", price_variance)
    print("Price Standard Deviation:", price_std_dev)
    
    print("\nPrice Movements:")
    print("Number of Positive Price Changes:", num_positive_changes)
    print("Number of Negative Price Changes:", num_negative_changes)
    print("Total Number of Price Changes:", total_changes)
    print("Average Positive Price Change:", avg_positive_change)
    print("Average Negative Price Change:", avg_negative_change)
