import pytest

from main import somar_dois_numeros, subtrair_dois_numeros, multiplicacao_dois_numeros, divisao_dois_numeros, \
    elevar_um_numero_pelo_outro, area_do_quadrado, area_do_triangulo, area_do_retangulo



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

    resultado_atual = area_do_quadrado(lado )
    assert resultado_atual == resultado_esperado

def testar_area_do_triangulo():
    base = 2
    altura = 3
    resultado_esperado = 3

    resultado_atual = area_do_triangulo(base, altura )
    assert resultado_atual == resultado_esperado

def testar_area_do_retangulo():
    base = 2
    altura = 3
    resultado_esperado = 6

    resultado_atual = area_do_retangulo(base, altura)
    assert resultado_atual == resultado_esperado