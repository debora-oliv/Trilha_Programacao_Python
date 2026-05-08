# %%
def verificar_permissao(permissoes_usuario: set, permissoes_exigidas: set):
    """
    Recebe o set de permissões do usuário e o set de permissões exigidas, retornando se ele tem todas as permissões necessárias para poder acessar (True ou False).
    """
    return permissoes_exigidas.issubset(permissoes_usuario) # ou usuando operador: permissoes_exigidas <= permissoes_usuario

usuario = {'read', 'write', 'delete', 'share'}
exigido = {'read', 'delete'}

print(verificar_permissao(usuario, exigido))