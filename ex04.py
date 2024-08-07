'''
Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade
expressa em dias. Escreva também um programa em Python para testar tal função.
'''
idade = 0
mes = 0 
dia = 0 
def idade_em_dias():
    dia_anos = idade*365
    dia_mes = mes*30
    idade_dias = dia_anos + dia_mes + dia
    return idade_dias
    
idade = int(input("Digite sua idade: "))
mes = int(input("Digite o mese atual: "))
dia = int(input("Digite o dia atual: "))

print("A didade em dias é: ", idade_em_dias())