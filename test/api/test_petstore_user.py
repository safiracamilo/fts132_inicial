# Bibliotecas
import pytest  # Framework de Teste Unitário - Engine
import requests  # Framework de Teste API - Requests / Responses

# Endereço da API
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}  # Nos .asmx seria 'text/xml'


# 0s  testes
def testar_criar_usuario():
    # Configura
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = "1212"

    # Executa
    resposta = requests.post(  # faz a requisição, passando:
        url=base_url,  # O endpoint da API
        data=open('C:/Users/SAFIRA/PycharmProjects/fts132_inicial/test/db/user1.json', 'rb'),  # O body JSON
        headers=headers  # O header com Content-Type
    )

    # Formatação
    corpo_da_resposta = resposta.json()  # Formata com JSON
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Resposta Formatada

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_consultar_usuario():
    # Configura
    status_code = 200
    id = 1212
    username = 'estrela'
    firstName = 'estrela'
    lastName = 'polar'
    emaiword = '124'
    email = 'estrelapolar@gmail.com'
    phone = '9999999999'
    userStatus = 0

    # executa
    resposta = requests.get(
        url=f'{base_url}/{username}',
        headers=headers
    )
    # Formatação
    corpo_da_resposta = resposta.json()  # Formata com JSON
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Resposta Formatada

    # Valida
    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['email'] == email
    assert corpo_da_resposta['phone'] == phone
