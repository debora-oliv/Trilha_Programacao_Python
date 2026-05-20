# %%
import pandas as pd

df = pd.read_csv("data/transacoes.csv", sep=";")
df

# %%
# SELECT * FROM df
df

# %%
# SELECT idCliente FROM df
df[["IdCliente"]]

# %%
# SELECT IdCliente, QtdePontos
# FROM df
# LIMIT 5
df[["IdCliente", "QtdePontos"]].tail(5)

# %%
# SELECT IdCliente, IdTransacao, QtdePontos
# FROM df
# LIMIT 10
df[["IdCliente", "IdTransacao", "QtdePontos"]].head(10)
