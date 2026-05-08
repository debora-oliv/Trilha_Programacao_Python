# %%
def habilidades_comum(habilidades: list):
    """
    Recebe uma lista contendo vários sets representando as habilidades de um candidato, retornando quais habilidades todos os candidatos possuem em comum.
    """

    comuns = habilidades[0]

    for hab_candidato in habilidades[1:]:
        comuns = comuns & hab_candidato

    return comuns

# %%
def habilidades_comum_desempacotamento(habilidades: list):
    """
    Recebe uma lista contendo vários sets representando as habilidades de um candidato, retornando as habilidades em comum,
    mas agora substituindo o laço de reptição pela função intersection que recebe os conjuntos de habilidades desempacotados.
    """
    return set.intersection(*habilidades) # equivalente à: set.intersection({'Python', 'SQL', 'Git'}, {'Docker', 'Python', 'Git'}, {'Python', 'AWS', 'Git', 'Linux'})

habilidades = [{'Python', 'SQL', 'Git'}, {'Docker', 'Python', 'Git'}, {'Python', 'AWS', 'Git', 'Linux'}]

# %%
print(habilidades_comum(habilidades))

# %%
print(habilidades_comum_desempacotamento(habilidades))