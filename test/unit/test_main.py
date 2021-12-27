import pytest

from main import somar_dois_numeros


def testar_somar_dois_numeros():
    # - 1 Etapa: Configura - Prepara
    # Dados - valores
    # Entrada - Input
    num1 = 4
    num2 = 5
    # saída - output
    resultado_esperado = 9

    # 2 Etapa: Executa
    resultado_atual=somar_dois_numeros(num1, num2)

    # 3 Etapa: Confirma - Valida
    assert resultado_atual == resultado_esperado