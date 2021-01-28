# QUESTÃO 01 - Escreva um programa que leia vários inteiros de um usuário e armazene-os em uma lista. Seu 
# programa deve continuar lendo valores até que seja digitado o valor 0. Ao final, ele deve imprimir todos os 
# valores inseridos pelo usuário (exceto o 0) de forma ordenada do menor para o maior.

numeros = []
numero = 1

while numero != 0:
    numero = int(input("Digite um número (Digite 0 (zero) para sair...): "))
    
    if numero != 0:
        numeros.append(numero)
    else:
        print("Foi digitado o número 0. Parando o programa...")
        break

for i in range(len(numeros)):
    print(f"O {i + 1}º número foi: {numeros[i]}")