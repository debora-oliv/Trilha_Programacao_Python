# %%
def unir_emails(emails_sistema1: list, emails_sistema2: list, emails_sistema3: list):
    """
    Recebe, imperativamente, três listas de e-mails de clientes vindas de sistemas diferentes, retornando uma única base de dados sem e-mails repetidos.
    """
    # cria uma nova lista contendo todos os elementos (incluindo os repetidos) apenas para entregá-la ao set() e depois descartá-la
    emails = emails_sistema1 + emails_sistema2 + emails_sistema3

    return set(emails)

def unir_emails_otimizado(*emails: list):
    """
    Recebe uma quantidade dinâmica de listas de e-mails, retornando uma única base de dados sem e-mails repetidos,
    mas agora usando union para juntar elementos de forma mais otimizada e levando em consideração a quantidade dinâmica.
    """
    return set().union(*emails)

l1, l2, l3, l4, l5 = ['a@a.com', 'b@b.com', 'e@e.com'], ['c@c.com', 'a@a.com'], ['b@b.com', 'd@d.com'], ['f@f.com'], ['e@e.com']

# %%
print(unir_emails(l1, l2, l3))

# %%
print(unir_emails_otimizado(l1, l2, l3, l4, l5))