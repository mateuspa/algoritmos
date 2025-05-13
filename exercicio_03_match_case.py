## Programa de Conversão de Moedas

## Para limpeza de tela
import os
os.system("cls") 

## rotina para conversão
while True:
    try:
        print(f"\nConversor de Real para moedas")
        opcao = int(input("\nDigite a opção para qual moeda você deseja converter:\n\n 1) Dolar\n 2) Euro\n 3) Libra\n 4) Sair do programa\n\n Opção desejada: "))

        match opcao:
            case 1:
                real = float (input("\nDigite um valor em Real: R$ "))
                print(f"\nR$ {real:.2f} = ${real/5.1:.2f}")
            case 2:
                real = float (input("\nDigite um valor em Real: R$ "))
                print(f"\nR$ {real:.2f} = €{real/6:.2f}")
            case 3:
                real = float (input("\nDigite um valor em Real: R$ "))
                print(f"\nR$ {real:.2f} = £{real/6.5:.2f}")
            case 4:
                print("\nObrigado. Volte logo!\n")
                break
            case _:
                print("\nOpção Inválida!!!\n")
        input("\nPressione ENTER para continuar")
        os.system("cls")
    except ValueError:
        print("\nOpção Inválida!!! Digite 1, 2, 3 ou 4.\n")
        input("\nPressione ENTER para continuar")