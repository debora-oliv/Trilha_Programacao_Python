import re
import requests
import streamlit as st

from requests.exceptions import RequestException

def coletar_texto_url(url: str) -> str:
    """
    Realiza uma requisição HTTP GET para obter o conteúdo de texto de uma URL.

    Args:
        url (str): O link direto para o arquivo de texto ou log na web.

    Returns:
        str: O texto bruto obtido da URL. Em caso de falha na requisição, 
             retorna uma string vazia.
    """
    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status() 
        
        return response.text

    # RequestException: classe base de erros da biblioteca requests
    except RequestException as erro:
        return ''

def escanear_vazamentos(texto: str, tipo_alvo: str) -> list[str]:
    """
    Varrer um texto em busca de padrões de dados sensíveis utilizando Expressões Regulares.

    Args:
        texto (str): O texto bruto onde a varredura será realizada.
        tipo_dado (str): O identificador do tipo de dado a ser buscado ('ip', 'email', 'data').

    Returns:
        list[str]: Uma lista contendo todas as strings que se enquadram no padrão.
                   Retorna uma lista vazia se nenhum vazamento for encontrado.
    """
    expression = ""

    match tipo_alvo:
        case "Email":
            expression = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
        case "IP":
            expression = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
        case "Data":
            expression = r"\b\d{4}-\d{2}-\d{2}\b"

    if not expression:
        return []

    return re.findall(expression, texto)

def renderizar_dashboard() -> None:
    """
    Constrói a interface web interativa do Scanner de Vazamentos utilizando Streamlit.
    
    A função renderiza o título, o campo de input de URL, os botões de execução 
    e as abas contendo os resultados extraídos.
    """
    url = st.text_input("Digite a URL")

    dado_alvo = st.radio("Escolha o tipo de dado que deseja varrer", ["Email", "Data", "IP"])

    if st.button("Procurar Vazamentos"):
        text = coletar_texto_url(url)
        st.write(escanear_vazamentos(text, dado_alvo))

renderizar_dashboard()
        


