# %%
import pandas as pd

df = pd.read_csv("data/transacoes.csv", sep=";")
df

# %%
# Filtra QtdePontos com valor maior ou igual à 50
filtro = df["QtdePontos"] >= 50
df[filtro]

# %%
# Filtra QtdePontos com valor entre 50 e 100
filtro = (df["QtdePontos"] > 50) & (df["QtdePontos"] < 100)
df[filtro]

# %%
# Filtra QtdePontos com valor igual à 1 ou igual à 100
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]

# %%
# Filtra QtdePontos com valor entre 0 e 25 ou do ano de 2025 para frente
filtro = (df["QtdePontos"]>=0) & (df["QtdePontos"]<=25) | (df["DtCriacao"]>='2025-01-01')
df[filtro]

# %%
# Filtra DescSistemaOrigem com valor igual à 'twitch'
filtro = (df["DescSistemaOrigem"] != 'twitch')
df[filtro]

# %%
# Filtra DescSistemaOrigem com valor igual à 'twitch' ou 'cursos'
filtro = df["DescSistemaOrigem"].isin(['twitch','cursos'])
df[filtro].sample(15)