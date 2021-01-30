# QUESTÃO 06 - Faça um programa que funciona como uma agenda telefônica. A agenda deve ser guardada em uma 
# lista com o seguinte formato: [[‘Ana’,‘99999-1234’], [‘Bia’, ‘99999-5678’]]. O programa deve ter um menu 
# que tenha as seguintes opções:
# 
# (a) Adicionar telefones na agenda -- isso deve ser feito de forma que ela se mantenha sempre ordenada -- 
# cada nome novo já deve ser inserido na posição correta dentro da agenda.

# (b) Procurar um telefone -- o usuário informa um nome e o programa mostra o número do telefone, ou diz que 
# não está na agenda. A busca deve ser inteligente: deve parar assim que encontrar um nome maior do que o nome 
# que está sendo buscado, ao invés de percorrer a lista sempre até o final para concluir que um nome não está 
# na agenda.

def criarContato(quantidadeContatos):
    return [[""]*2 for i in range(quantidadeContatos)]

def menu():
    print("\t\tMENU DE OPÇÕES \n \na. Adicionar telefones na agenda \nb. Procurar um telefone\n")


menu()
listaContatos = ""
opcao = input("Digite uma das opções acima: ")

if opcao.upper() == "A":
    print("\nADICIONAR CONTATO: ")
    
    quantidadeContatos = int(input("Quantos contados deseja adicionar? "))
    listaContatos = criarContato(quantidadeContatos)

    for i in range(quantidadeContatos):
        for j in range(1):
            listaContatos[i][j] = input("Digite o nome: ")
            listaContatos[i][j + 1] = input("Digite o telefone: ")

    print("Contatos cadastrados!!")

menu()
opcao = input("Digite uma das opções acima: ")

if opcao.upper() == "B":
    print("\nBUSCAR CONTATO: ")

    nomeContato = input("Digite o nome do contato que deseja encontrar: ")
    for i in listaContatos:
        if nomeContato == i[0]:
            print(f"Nome: {i[0]}\nTelefone: {i[1]}")

        else:
            print("Contato inexistente!!")