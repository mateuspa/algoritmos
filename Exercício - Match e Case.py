import os
os.system("cls")

# Saldo inicial da conta
saldo = 0

while True:
    print("\n===== CAIXA ELETRÔNICO FATEC =====")
    print("1 - Saldo")
    print("2 - Saque")
    print("3 - Depósito")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            print(f"\n$$$$ Seu saldo atual é R$ {saldo:.2f} $$$$")

        case "2":
            valor = float(input("Digite o valor para saque: R$ "))
            if valor > saldo:
                print("\nSaldo insuficiente!")
            else:
                saldo -= valor
                print(f"\nSaque de R$ {valor:.2f} realizado.\n\n$$$$ Novo saldo: R$ {saldo:.2f} $$$$")

        case "3":
            valor = float(input("Digite o valor para depósito: R$ "))
            saldo += valor
            print(f"\nDepósito de R$ {valor:.2f} realizado.\n\n$$$$ Novo saldo: R$ {saldo:.2f} $$$$")

        case "4":
            print("\nSaindo... Obrigado por utilizar nosso caixa eletrônico!\n")
            break

        case _:
            print("Opção inválida. Escolha uma opção válida.")