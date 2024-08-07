'''
Escreva uma função que receba um número inteiro e o imprima na forma extensa. Por exemplo,
para 1 a saída desejada é “Um”. A função deve ser capaz de gerar o extenso dos números de 0 até
10, inclusive. Caso um número não compatível seja recebido o procedimento deve mostrar uma
mensagem de erro. Escreva também um programa em Python para testar tal função.
'''
def num (n1):
    if n1 == 0:
        print('Zero')
    elif n1 == 1:
        print('Um')
    elif n1 == 2:
        print('Dois')
    elif n1 == 3:
        print('Três')
    elif n1 == 4:
        print('Quatro')
    elif n1 == 5:
        print('Cinco')
    elif n1 == 6:
        print('Seis')
    elif n1 == 7:
        print('Sete')
    elif n1 == 8:
        print('Oito')
    elif n1 == 9:
        print('Nove')
    elif n1 == 10:
        print('Dez')
    else:
        print('Número inválido')



num(2)
num(5)
num(14)
