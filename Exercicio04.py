# QUESTÃO 04 - Faça um programa que percorre um vetor e imprime na tela o valor mais próximo da média dos 
# valores do vetor. Exemplo: vetor = [2.5, 7.5, 10.0, 4.0]
# 
# (média = 6.0)
# Valor mais próximo da média = 7.5
notas = []
nota = "0"
notaMaisProxima = 0.0
media = 0.0

def valorProximo(notas):
    global media
    for i in range(len(notas)):
        media += notas[i]

    media = media / len(notas)
    diffs = {value: abs(value - media) for value in notas}
    print(f"Média = {media}")
    return min(diffs, key=diffs.get)

while nota != "":
    nota = input("Digite uma nota: ")
    if nota != "":
        notas.append(float(nota))

print(f"O valor mais próximo da média é: {valorProximo(notas)}")