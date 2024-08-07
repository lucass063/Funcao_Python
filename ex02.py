'''
Faça uma função que recebe um valor inteiro e verifica se o valor é positivo, negativo ou zero. A
função deve retornar 1 para valores positivos, -1 para negativos e 0 para o valor 0. Escreva
também um programa em Python para testar tal função.
'''
def num(n1):
    if n1 > 0:
        return 1
    elif n1 < 0:
        return -1
    else:
        return 0



print(num(6))  
print(num(-2))  
print(num(0))   