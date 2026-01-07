import pandas as pd

df = pd.read_excel('datasets/Europe_Rent_2025.xlsx')
print(df.head())

print(df.columns)        # nomes das colunas
df.rename(columns={'Rent (�)': 'Rent (€)'}, inplace=True)
print(df.dtypes)         # tipos de dados
#print(df.info())         # resumo do DataFrame
#print(df.describe())     # estatísticas básicas
