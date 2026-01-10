import pandas as pd

df = pd.read_csv(
    'datasets/house-data.csv',
    sep=',',           # vírgula
)

print(df.head(10))

#print(df.info())


