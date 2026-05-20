# %%
import pandas as pd

df = pd.read_csv("data/clientes.csv", sep=";")
df

# %%
# Coverte 'qtdePontos' para float 
df["qtdePontos"].astype(float)

# %%
# Coverte 'qtdePontos' para float e depois para string
df["qtdePontos"].astype(float).astype(str)

# %%
# Cria um dicionpário no formato {"valor_atual":"valor_novo"} para passar como argumento na função replace()
replace = {"0000-00-00 00:00:00.000": "2025-01-01 09:00:00.000"}

# Coverte 'DtCriacao' para datetime após substituir os valores do df indicados no dicionário
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))
df["DtCriacao"].dt.month.tail(5)