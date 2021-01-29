# QUESTÃO 05 - Faça um programa que percorre duas listas e intercala os elementos de ambas, formando uma 
# terceira lista. A terceira lista deve começar pelo primeiro elemento da lista menor. Exemplo:
# 
# lista1 = [1, 2, 3, 4]
# lista2 = [10, 20, 30, 40, 50, 60]
# lista_intercalada = [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]

listaUm = []
listaDois = []
listaTres = []

for i in range(5):
    listaUm.append(int(input(f"Digite o {i + 1}º valor da 1º lista: ")))
    listaDois.append(int(input(f"Digite o {i + 1}º valor da 2º lista: ")))

for i in range(5):
    listaTres.append(listaUm[i])
    listaTres.append(listaDois[i])

print(f"Lista 01: {listaUm}")
print(f"Lista 02: {listaDois}")
print(f"Lista 03: {listaTres}")