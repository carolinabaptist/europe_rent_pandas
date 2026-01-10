import pandas as pd

df = pd.read_csv(
    'datasets/house-data.csv',
    sep=',',           # vírgula
    engine='python',   # necessário para linhas muito longas
    low_memory=False,  # evita erros de tipos de dados mistos
    encoding='utf-8'
)

print(df.head(10))

#print(df.info())


