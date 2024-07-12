"""
=========================================================================
Aplicativo que simula operações bancárias em modo texto
usado para exemplificar a usabilidade de
while, if, elif, f string, lista, variáveis, tipos de dados, constantes,
operadores lógicos e de atribuição
-------------------------------------------------------------------------
Autor: Alecsandro Melo
Baseado no Desafio do Módulo Dominando Python e Suas Estruturas do
Bootcamp Python Ai Backend Developer da plataforma Dio -> (www.dio.me)
=========================================================================
"""

# Variáveis e Constantes
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

#Tela Inicial
menu_inicio = """
================ Banco =================
[d] Depositar
[s] Sacar
[e] Extrato
[f] Fechar

Digite uma Opção: """

#inicio do loop condicional
while True:

    #Entrada da Opção do Menu pelo usuário
    opcao = input(menu_inicio)

    #Opção depósito
    if opcao == "d":
        valor_deposito = float(input("Digite o valor do Depósito: "))
        if valor_deposito > 0:
            #Incrementa valor do saldo
            saldo += valor_deposito

            #Adiciona movimentação na lista Extrato
            extrato.append(f"Depósito no valor de: R${valor_deposito:.2f}")
            print(f"Deposito realizado com sucesso, seu saldo é: R${saldo:.2f}\n")
            
        else:
            print("Valor informado é inválido")
                                                           
    #Opção saque
    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque desejado: "))

        #regras condicionais 
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Valor informado é maior que saldo disponível")

        elif excedeu_limite:
            print("Valor informado é maior que seu limite por operação")

        elif excedeu_saques:
            print("Excedeu o limite de saques diários")

        else:
            #decrementa valor do saldo
            saldo -= valor_saque

            #Adiciona movimentação na lista Extrato
            extrato.append(f"Saque no valor de: R${valor_saque:.2f}")
            print(f"Saque realizado com sucesso, retire o valor: R${valor_saque:.2f}\n")

            #incrementa numero de saques
            numero_saques += 1
        
    #Opção Extrato - Exibe valor do saldo e movimentações
    elif opcao == "e":
            
            print(f"Extrato".center(40, "=") + "\n")

            #Testa de a lista extrato é vázia
            if not extrato:
                print("Ainda não foram realizadas movimentações")

            else:
                print(f" Seu saldo atual é: R${saldo:.2f}\n")
                print(f"Histórico".center(40, "=") + "\n")

                #iteração da lista extrato para exibir movimentações linha a linha
                for movimentacoes in extrato:
                    print(f"{movimentacoes}")
        
    #Encerra o Loop
    elif opcao == "f":
        
        break

    #Caso nenhuma opção seja válida exibe mensagem na tela 
    else:
        
        print("Operação inválida, por favor escolha a operação desejada.")


