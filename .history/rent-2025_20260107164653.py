import pandas as pd

df = pd.read_excel('datasets/Europe_Rent_2025.xlsx')
#print(df.head(10))
#print(df.tail(5))

print(df.columns)        # nomes das colunas
#print(df.dtypes)         # tipos de dados
#print(df.info())         # resumo do DataFrame
#print(df.describe())     # estatísticas básicas

#print(df['City Centre']) # pegar só os nomes das cidades
#print(df["Rent"].max())
#print(df["Rent"].min())

#print(df.iloc[5]) # em formato de Series, mostra a linha 5

# cidades com aluguel acima de 2000€
#high_rent = df[df['Rent'] > 2000]
#print(high_rent)

#ordenar dados
df_sorted = df.sort_values('Rent (€)', ascending=False)
print(df_sorted.head())
