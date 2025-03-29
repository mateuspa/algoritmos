saldo = 10000  # Saldo inicial da conta

while True:
    print("\n===== CAIXA ELETRÔNICO FATEC =====")
    print("1 - Saldo")
    print("2 - Saque")
    print("3 - Depósito")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print(f"Seu saldo atual é R$ {saldo:.2f}")

        case "2":
            valor = float(input("Digite o valor para saque: "))
            if valor > saldo:
                print("Saldo insuficiente!")
            else:
                saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {saldo:.2f}")

        case "3":
            valor = float(input("Digite o valor para depósito: "))
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {saldo:.2f}")

        case "4":
            print("Saindo... Obrigado por utilizar nosso caixa eletrônico!")
            break

        case _:
            print("Opção inválida. Escolha uma opção válida.")