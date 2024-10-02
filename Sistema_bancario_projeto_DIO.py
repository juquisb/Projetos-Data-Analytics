menu = """ ========= Bem-vindo ao sistema de caixa eletrônico do Banco System ========

Selecione a opção desejada:

[1] Saque
[2] Depósito
[3] Extrato
[4] Sair

Opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        print("Saque")
        saque = float(input("Informe o valor a ser sacado: "))

        if saque <= 0:
            print("Valor inválido. O valor de saque deve ser positivo.")
        elif saque > saldo:
            print("Saldo insuficiente.")
        elif saque > limite:
            print(f"O valor do saque excede o limite permitido de R$ {limite:.2f}.")
        elif numero_saques >= limite_saques:
            print("Limite de saques diários excedido.")
        else:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso, seu saldo é de: R$ {saldo:.2f}")

    elif opcao == '2':
        print("Depósito")
        deposito = float(input("Informe o valor a ser depositado: "))
        
        if deposito <= 0:
            print("Valor inválido. O valor de depósito deve ser positivo.")
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito realizado com sucesso, seu saldo é de: R$ {saldo:.2f}")

    elif opcao == '3':
        print("Extrato")
        print("\n========= EXTRATO =========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("============================\n")

    elif opcao == '4':
        print("Saindo, obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida, por favor selecione novamente.")
