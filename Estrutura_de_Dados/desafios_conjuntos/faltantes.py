# %%
def faltantes(ids_esperados: list, ids_sobreviventes: list):
    """
    Receba uma lista sequencial de IDs que deveriam ter sido gerados pelo sistema e os IDs que de fato o sistema gerou, retornando quais IDs sumiram/faltaram.
    """
    return set(ids_esperados)-set(ids_sobreviventes) # versão mais otimizada: set(ids_esperados).difference(ids_sobreviventes)

esperados = range(1, 21)
sobreviventes = [1, 2, 3, 5, 7, 8, 9, 14, 15, 19]

print(faltantes(esperados, sobreviventes))