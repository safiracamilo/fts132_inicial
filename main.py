#def somar_dois_numeros(num1,num2):
    #soma = num1 + num2
    #print(f'A Soma é {soma}')

#if __name__ == '__main__':
    #somar_dois_numeros(5,8)

import math

def somar_dois_numeros(num1,num2):
    return num1 + num2

def subtrair_dois_numeros(num1,num2):
    return num1 - num2

def multiplicacao_dois_numeros(num1,num2):
    return num1 * num2

def divisao_dois_numeros(num1,num2):
    try:
        return num1 / num2
    except:
        return 'não é possível dividir por zero'

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

def area_do_quadrado(lado):
    return  lado * lado

def area_do_triangulo(base, altura):
    return  (base * altura) / 2


def area_do_retangulo(base, altura):
    return  base* altura

def area_do_circulo(raio):
    try:
        return 3.14 * raio ** 2
    except TypeError:

        return 'Falha no calculo - Raio não e um número'

def volume_do_paralelograma(largura, comprimento, altura):
    return largura * comprimento * altura

def raiz_quadrada(num1):
    return math.sqrt(num1)

if __name__ == '__main__':

    soma = somar_dois_numeros(10,3)
    print(f'A Soma é {soma}')

    subtracao = subtrair_dois_numeros(5,7)
    print(f'A Subtração é: {subtracao}')


    multiplicacao = multiplicacao_dois_numeros(7, 5)
    print(f'A multiplicacao é: {multiplicacao}')

    divisao = divisao_dois_numeros(10, 0)
    print(f'A divisao é: {divisao}')

    potencia = elevar_um_numero_pelo_outro(2, 3)
    print(f'A exponeciacão é: {potencia}')

    quadrado = area_do_quadrado(10)
    print(f'A área do quadrado é: {quadrado}')

    triangulo = area_do_triangulo(2, 3)
    print(f'A área do triangulo é: {triangulo}')

    retangulo = area_do_retangulo(2, 3)
    print(f'A área do retangulo é: {retangulo}')

    circulo = area_do_circulo(1)
    print(f'A área do circulo é: {circulo}')

    raiz = raiz_quadrada(10)
    print(f'A raiz do é: {raiz}')

'''
import pytest
    #Teste(Desgutador)

def testar_somar_dois_numeros():
    # - 1 Etapa: Configura - Prepara
    # Dados - valores
    # Entrada - Input
    num1 = 8
    num2 = 9
    # saída - output
    resultado_esperado = 17

    # 2 Etapa: Executa
    resultado_atual=somar_dois_numeros(num1, num2)

    # 3 Etapa: Confirma - Valida
    assert resultado_atual == resultado_esperado
'''





