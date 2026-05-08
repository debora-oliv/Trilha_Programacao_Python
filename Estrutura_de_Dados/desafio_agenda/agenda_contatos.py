# %%
agenda = {}

def adicionar_contato(telefone: str, nome: str, sobrenome: str, email: str):
    """
    Recebe informações de contato de uma pessoa, adicionando o contato apenas se o telefone não existir na agenda.
    Se o telefone já existir, exibe uma mensagem avisando que o contato já existe.
    """
    if telefone in agenda:
        print("O contato informado já existe.")
    else:
        agenda[telefone] = {'nome': nome, 'sobrenome': sobrenome, 'email': email}


def buscar_contato(telefone: str):
    """
    Recebe um telefone, retornando os dados do contato, se exisitir.
    Se o contato não existir, exibe uma mensagem avisando que o contato não foi encontrado.
    """
    return agenda.get(telefone, "O contato não foi encontrado.") # assume o valor da chave informada, caso encontre em agenda, ou assume a mensagem de aviso


def atualizar_contato(telefone: str, novo_nome: str = None, novo_sobrenome: str = None, novo_email: str = None):
    """
    Atualiza os campos fornecidos de um contato, enquanto os campos não fornecidos assumem o valor padrão (None) e são ignorados.
    """
    if telefone not in agenda:
        print("Contato não encontrado.")
        return

    if novo_nome:
        agenda[telefone]['nome'] = novo_nome
    if novo_sobrenome:
        agenda[telefone]['sobrenome'] = novo_sobrenome
    if novo_email:
        agenda[telefone]['email'] = novo_email
        

def remover_contato(telefone: str):
    """
    Remove completamente o contato da agenda.
    """
    agenda.pop(telefone, "Contato não encontrado.")


# %%
adicionar_contato('9999-1111', 'Ana', 'Almeida', 'ana@email.com')
adicionar_contato('9999-2222', 'Fernando', 'Soares', 'fernanda@email.com')
adicionar_contato("9999-3333", "Sebastião", "Maia", "sebastiao@email.com")
adicionar_contato('9999-1111', 'Ana', 'Soares', 'ana@email.com')

# %%
atualizar_contato('9999-2222', novo_nome='Fernanda', novo_email='fernanda@email.com')
atualizar_contato('9999-3333', novo_sobrenome='Oliveira')
print(agenda)
atualizar_contato('0000-0000', novo_sobrenome='Barbosa')

# %%
print(buscar_contato('9999-3333'))
print(buscar_contato('0000-0000'))

# %%
remover_contato('9999-3333')
remover_contato('0000-0000')

# %%
print(agenda)
# %%
