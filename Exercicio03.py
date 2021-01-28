# QUESTÃO 03 - Faça um programa que simule um lançamento de dados. Lance o dado 10 vezes e armazene os 
# resultados em um vetor. Depois, monte um outro vetor contendo quantas vezes cada valor foi obtido. Imprima 
# os dois vetores. Use uma função para gerar números aleatórios, simulando os lançamentos dos dados. Exemplo 
# de uma possível saída:
# 
# [3, 1, 5, 3, 5, 4, 5, 5, 3, 6]
# [1, 0, 3, 1, 4, 1]

from random import randint, uniform

lancamentos = []
quantidadeLancamentos = []

def lancaDados():
    for i in range(10):  
        random = (randint(1, 6))
        lancamentos.append(random)
        print(f"O {i + 1}º lançamento exibiu o número {lancamentos[i]}")
    
    return lancamentos

lancaDados()

for i in range(6):
    quantidadeLancamentos.append(lancamentos.count(i + 1))
    print(f"O número {i + 1} do dado foi exibido {quantidadeLancamentos[i]} vezes")
