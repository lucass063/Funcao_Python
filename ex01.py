'''
Crie uma função que converta graus Celsius para Fahrenheit. Escreva também um programa em
Python para testar tal função.
'''
def converte(c):
    f = (c * 9/5) + 32
    return f

# Testando a função
print(converte(1))