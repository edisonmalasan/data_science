import pandas as pd

file_path = 'assets/prelims/raw.csv'
df = pd.read_csv(file_path)

cols = ['Age', 'Quantity', 'Price per Unit', 'Total Amount']
mode_cols = ['Date', 'Gender', 'Age', 'Product Category', 'Quantity', 'Price per Unit', 'Total Amount']

print("\nMEAN")
for col in cols: print(f"Mean [{col}]: {df[col].mean()}")

print("\nMEDIAN")
for col in cols: print(f"Median [{col}]: {df[col].median()}")

print("\nMODE")
for col in mode_cols: print(f"Mode [{col}]: {df[col].mode()[0]}")

print("\nVARIANCE")
for col in cols: print(f"Variance [{col}]: {df[col].var():.4f}")

print("\nSTANDARD DEVIATION")
for col in cols: print(f"STD [{col}]: {df[col].std():.4f}")