import pandas as pd

df = pd.read_csv('datasets/house-data.csv', sep=';', engine='python', encoding='utf-8')
print(df.head(10))

#print(df.info())


