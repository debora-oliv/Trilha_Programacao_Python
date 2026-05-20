# %%
import pandas as pd

df_clientes = pd.read_csv("data/clientes.csv", sep=";")
df_clientes

# %%
df_clientes.head(7) # exibe as 7 primeiras linhas

# %%
df_clientes.tail(7) # exibe as 7 últimas linhas

# %%
df_clientes.sample(7) # exibe 7 linhas aleatórias

# %%
df_clientes.index

# %%
df_clientes.columns

# %%
df_clientes.shape

# %%
# Retorna uma Serie com valores de uma coluna especificada
df_clientes["flYouTube"]

# %%
# Retorna uma Serie com colunas e valores de uma linha específica (nesse caso, a primeira linha)
df_clientes.iloc[0]

# %%
# Retorna uma Serie com colunas e valores de uma linha específica (nesse caso, a última linha)
df_clientes.iloc[-1]

# %%
# Retorna um Dataframe com colunas e valores das linhas de um intervalo especificado (nesse caso, da linha 1 até linha 3)
df_clientes.iloc[:3]

# %%
# Retorna todo o Dataframe, porém de trás para frente 
df_clientes.iloc[::-1]

# %%
# Retorna o valor de uma coluna especificada da linha (nesse caso, da primeira linha)
df_clientes.iloc[0]["idCliente"]

# %%
# Retorna o valor de uma coluna especificada da linha (nesse caso, da última linha)
df_clientes.iloc[-1]["idCliente"]

# %%
# Cria uma nova coluna com a soma dos valores de todas as colunas especificadas
df_clientes["todas_social"] = df_clientes["flEmail"] + df_clientes["flTwitch"] + df_clientes["flYouTube"] + df_clientes["flBlueSky"] + df_clientes["flInstagram"]
df_clientes.sample(15)
