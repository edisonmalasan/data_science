import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/INSTRUCT-D522lab/Desktop/data_science/assets/prelims/animal_data_dirty1.csv', sep=';')
df.head(5)
print(df.head())

df.info()
df.describe()

print(f'shape: {df.shape}')



