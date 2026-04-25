#AI lab task 09:
import pandas as pd
file_name = 'amazon.csv'
dataset = pd.read_csv(file_name)
print("--- first 5 Rows ---")
print(dataset.head())
print("\n--- last five Rows ---")
print(dataset.tail())
print(f"\nRows: {dataset.shape[0]}")
print(f"columns: {dataset.shape[1]}")
print("\n--- Null columns ---")
print(dataset.isnull().sum())
dataset = dataset.fillna(dataset.mode().iloc[0])
print("\n--- Data Types ---")
print(dataset.dtypes)
