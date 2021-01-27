# QUESTÃO 02 - Faça um programa que percorre uma lista com o seguinte formato: 
# [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], 'Itália', 'Espanha', [7,8]]]. 
# Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e 
# Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela:
# (a) o total de faltas do campeonato
# (b) o time que fez mais faltas
# (c) o time que fez menos faltas

tabelaFaltas = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], 'Itália', 'Espanha', [7,8]]

totalFaltas = tabelaFaltas[0][2][0] + tabelaFaltas[0][2][1] + tabelaFaltas[1][2][0] + tabelaFaltas[1][2][1] + tabelaFaltas[4][0] + tabelaFaltas[4][1]
timeMaisFaltas = tabelaFaltas[0][0]
timeMenosFaltas = tabelaFaltas[1][0]
print
(f"O total de faltas do campeonato foi: {totalFaltas}")
print(f"O time que mais cometeu faltas foi: {timeMaisFaltas} no jogo {tabelaFaltas[0][0]} X {tabelaFaltas[0][1]}")
print(f"O time que menos cometeu faltas foi: {timeMenosFaltas} no jogo {tabelaFaltas[1][0]} X {tabelaFaltas[1][1]}")