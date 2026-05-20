# %%
import pandas as pd

df = pd.DataFrame({
    "nome": ['teo', None, 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    "sobrenome": ['calvo', None, 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
    "salario": [3453, None, None, 5423, 6532, 4322, 1987, 2134],
    "idade": [None, None, 43, 52, 50, 33, 39, 41]
})

df

# %%
# Remove todas as linhas com ao menos um None/NaN
df.dropna()

# %%
# Remove apenas linhas com todos os valores iguais a None/NaN
df.dropna(how="all")

# %%
# Remove apenas linhas com valores de idade e salario iguais a None/NaN
df.dropna(how="all", subset=["idade", "salario"])

# %%
# Remove apenas as linhas com valores de idade ou salario iguais a None/NaN
df.dropna(how="any", subset=["idade", "salario"])

# %%
# Substitui todos os None/NaN de uma coluna por um valor especificado
df["idade"] = df["idade"].fillna(0)
df

# %%
# Substitui todos os None/NaN de mútiplas colunas por valores especificados em formato de dicionário {"coluna":"valor_substituto"}
df.fillna({"nome": "fulano", "idade": 0})

# %%
# Substitui todos os None/NaN das colunas 'idade' e 'salario' por suas respectivas médias
medias = df[['idade', 'salario']].mean()
df.fillna(medias)

# %%
# Remove todas as duplicatas mantendo apenas a primeira aparição
df.drop_duplicates(keep='first')

# %%
# Remove linhas com valores de 'nome' e 'sobrenome' duplicados mantendo apenas a primeira aparição
df.drop_duplicates(keep='first', subset=["nome", "sobrenome"])

# %%
# Remove linhas com valores de 'nome' e 'sobrenome' duplicados mantendo apenas a útilma aparição
df.drop_duplicates(keep='last', subset=["nome", "sobrenome"])