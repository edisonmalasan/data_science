import pandas as pd

df = pd.read_csv('C:/Users/INSTRUCT-D522lab/Desktop/data_science/assets/prelims/LIVESTOCK.csv')

columns = [
    "Farm",
    "Livestock_Production_heads_per_year",
    "Annual_Rainfall_mm",
    "Fertilizer_Use_kg_per_ha",
    "Crop_Price_USD_per_ton"
]

for col in columns:
    print(
        f"{col}: "
        f"[Mean]= {df[col].mean():.2f}, "
        f"[Std]= {df[col].std():.2f}, "
        f"[Q1]= {df[col].quantile(0.25):.2f}, "
        f"[Q3]= {df[col].quantile(0.75):.2f}, "
        f"[5th]= {df[col].quantile(0.05):.2f}, "
        f"[95th]= {df[col].quantile(0.95):.2f}"
    )