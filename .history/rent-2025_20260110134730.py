import pandas as pd

df = pd.read_excel('datasets/house-data.xlsx')

#print(df.head(10))
print(df.info())
print(df.describe())
