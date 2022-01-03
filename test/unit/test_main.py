import csv

import pytest

from main import somar_dois_numeros, subtrair_dois_numeros, multiplicacao_dois_numeros, divisao_dois_numeros, \
    elevar_um_numero_pelo_outro, area_do_quadrado, area_do_triangulo, area_do_retangulo, area_do_circulo, \
    volume_do_paralelograma, volume_do_cilindro


def testar_somar_dois_numeros():
    # - 1 Etapa: Configura - Prepara
    # Dados - valores
    # Entrada - Input
    num1 = 4
    num2 = 5
    # saída - output
    resultado_esperado = 9

    # 2 Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # 3 Etapa: Confirma - Valida
    assert resultado_atual == resultado_esperado


def testar_subtrair_dois_numeros():
    num1 = 1
    num2 = 1
    resultado_esperado = 0

    resultado_atual = subtrair_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_multiplicacao_dois_numeros():
    num1 = 2
    num2 = 2
    resultado_esperado = 4

    resultado_atual = multiplicacao_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_divisao_dois_numeros():
    num1 = 10
    num2 = 2
    resultado_esperado = 5

    resultado_atual = divisao_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_elevar_um_numero_pelo_outro():
    num1 = 2
    num2 = 2
    resultado_esperado = 4

    resultado_atual = elevar_um_numero_pelo_outro(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_area_do_quadrado():
    lado = 2
    resultado_esperado = 4

    resultado_atual = area_do_quadrado(lado)
    assert resultado_atual == resultado_esperado


def testar_area_do_triangulo():
    base = 2
    altura = 3
    resultado_esperado = 3

    resultado_atual = area_do_triangulo(base, altura)
    assert resultado_atual == resultado_esperado


def testar_area_do_retangulo():
    base = 2
    altura = 3
    resultado_esperado = 6

    resultado_atual = area_do_retangulo(base, altura)
    assert resultado_atual == resultado_esperado


@pytest.mark.parametrize('raio, altura, resultado_esperado', [
    # valores
    (4, 5, 251.20000000000002),  # teste n.1
    (1, 2, 6.28),
    (3, 4, 113.04)

])
def testar_volume_do_cilindro(raio, altura, resultado_esperado):
    # raio = 4
    # altura = 5
    # resultado_esperado = 251.20000000000002

    resultado_atual = volume_do_cilindro(float(raio), float(altura), float(resultado_esperado))
    assert resultado_atual == (resultado_esperado)


# anotação para utilizar como massa de teste
def ler_dados_csv():
    dados_csv = []  # criação de uma lista vazia
    nome_arquivo = 'C:/Users/SAFIRA/PycharmProjects/fts132_inicial/test/db/massa_caixa.csv'  # local e nome onde está o arquivo de massa
    try:
        with open(nome_arquivo, newline='') as csvfile:  # repetir a leitura até o fim do arquivo
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileExistsError:
        print(f'Arquivo não encontrado:{nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista:{fail}')


@pytest.mark.parametrize('id,largura,comprimento,altura,resultado_esperado', ler_dados_csv())
def testar_volume_do_paralelograma(id, largura, comprimento, altura, resultado_esperado):
    '''
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100
    '''

    resultado_atual = volume_do_paralelograma(int(largura), int(comprimento), int(altura))
    assert resultado_atual == int(resultado_esperado)


# Para fazer o teste de lista primeiro preenche a lista com parametros a serem executados na função.
@pytest.mark.parametrize('raio,resultado_esperado', [
    # valores
    (1, 3.14),  # teste n.1
    (2, 12.56),  # teste n.2
    (3, 28.26),  # teste n.3
    (4, 50.24),  # teste n.4
    ('a', 'Falha no calculo - Raio não e um número'),  # teste n.5
])

# cada linha da lista acima será executada na função abaixo:
def testar_area_do_circulo(raio, resultado_esperado):
    # raio = 1 (Comentei para que os parametros seja lidos
    # resultado_esperado = 3.14

    resultado_atual = area_do_circulo(raio)
    assert resultado_atual == resultado_esperado


# ler dados de csv para usar no tete seguinte


def ler_dados_csv1():
    dados_csv = []  # criação de uma lista vazia
    nome_arquivo = 'C:/Users/SAFIRA/PycharmProjects/fts132_inicial/test/db/massa_volume.csv'  # local e nome onde está o arquivo de massa
    try:
        with open(nome_arquivo, newline='') as csvfile:  # repetir a leitura até o fim do arquivo
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileExistsError:
        print(f'Arquivo não encontrado:{nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista:{fail}')


@pytest.mark.parametrize('id,raio,altura,resultado_esperado', ler_dados_csv1())
def testar_volume_do_cilindro2(id,raio, altura, resultado_esperado):
    resultado_atual = volume_do_cilindro(float(raio), float(altura))

    assert resultado_atual == float(resultado_esperado)
