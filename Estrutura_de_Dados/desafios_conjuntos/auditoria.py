# %%
def auditoria(mes_passado: list, mes_atual: list):
    """
    Recebe duas listas (IDs de produtos do mês passado e IDs deste mês), retornando os produtos novos que entraram e os produtos antigos que saíram de linha.
    """
    return set(mes_passado)-set(mes_atual), set(mes_atual)-set(mes_passado) # (removidos, adicionados)

mes_passado = [1, 2, 3, 4, 5]
mes_atual = [4, 5, 6, 7]

# %%
print(auditoria(mes_passado, mes_atual))