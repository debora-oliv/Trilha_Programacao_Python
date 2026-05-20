# %%
import pandas as pd

clientes = pd.read_csv("data/clientes.csv", sep=";")
clientes

# %%
# Ordena de maneira decrescente seguindo como base 'qtdePontos'
top_5 = clientes.sort_values(by="qtdePontos", ascending=False).head(5)
top_5

# %%
# Ordena de maneira decrescente tanto 'qtdePontos' quanto 'flTwitch'
top_5 = clientes.sort_values(by=["qtdePontos", "flTwitch"], ascending=False).head(5)
top_5

# %%
# Ordena de maneira decrescente 'qtdePontos' e de maneira crescente 'flTwitch'
top_5 = clientes.sort_values(by=["qtdePontos", "flTwitch"], ascending=[False, True]).head(5)
top_5