import pytest
import requests

base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}  # Nos .asmx seria 'text/xml'


def testar_incluir_pet():
    #Configura
    #Dados de Entrada
    status_code_esperado = 200
    nome_pet_esperado = 'Liz'
    tag_esperada = 'vacinado'

    #Executa
    resposta = requests.post(  # faz a requisição, passando:
        url=base_url,  # O endpoint da API

        data=open('C:/Users/SAFIRA/PycharmProjects/fts132_inicial/test/db/pet1.json', 'rb'),  # O body JSON
        headers=headers  # O header com Content-Type
    )
    # Formatação
    corpo_da_resposta = resposta.json()  # Formata com JSON
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Resposta Formatada

    # Valida.
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta ['name'] == nome_pet_esperado
    assert corpo_da_resposta ['tags.name'] == tag_esperada



