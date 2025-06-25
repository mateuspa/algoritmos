# função para calcular o peso de latas de alumínio em gramas
def peso(n):
    peso_lata = 14.5 # peso de uma lata de alumínio em gramas
    return n * peso_lata

# função para calcular o valor das latas
def valor(n):
    valor_kilo_lata = 5 # valor em reais por kg de alumínio
    return valor_kilo_lata * peso(n) / 1000

# função para calcular a quantidade de CO2eq emitida por kg de alumínio produzido
def co2(n):
    co2_por_g = 4.2 # g de CO2eq emitidos por g de alumínio
    return n * co2_por_g

while True:
    try:
        print(f"\nCálculos para o PI - latas de alumínio\n")
        opcao = int(input("Digite a opção para calcular: \n\n 1) O peso de uma quantidade de latas de alumínio\n 2) O valor (R$) de uma quantidade de latas de alumínio\n 3) A quantidade de CO2 emitido para produzir determinado peso de alumínio\n 4) Sair do programa\n\n Opção desejada: "))
        match opcao:
            case 1:
                print ("\nCalculadora de peso de latas de alumínio\n")
                n = float(input("Digite a quantidade de latas de alumínio (considerando 14,5 g por lata): "))
                if n <= 0:
                    print("Quantidade de latas inválida! Digite uma quantidade maior que zero.")                
                else:
                    print(f"O peso de {n:.0f} lata(s) é igual a: {peso(n):.2f} g")
            case 2:
                print ("\nCalculadora de valor de latas de alumínio\n")
                n = float(input("Digite a quantidade de latas de alumínio (considerando R$ 5,00 por kg de alumínio): "))
                if n <= 0:
                    print("Quantidade de latas inválida! Digite uma quantidade maior que zero.")                
                else:
                    print(f"O valor de {n:.0f} lata(s) é igual a: R$ {valor(n):.2f}")
            case 3:
                print ("\nCalculadora de emissão de CO2 para produção de latas de alumínio\n")
                n = float(input("Digite a quantidade de latas de alumínio (considera 4,2 g por lata): "))
                if n <= 0:
                    print("Quantidade de latas inválida! Digite uma quantidade maior que zero.")                
                else:
                    print(f"A quantidade de CO2 emitida para a produção de {n:.0f} lata(s) é igual a: {co2(n):.2f} g CO2eq")
            case 4:
                print("\nObrigado. Volte logo!\n")
                break
            case _:
                print("\nOpção Inválida. Digite 1, 2, 3 ou 4.\n")
        input("\nPressione ENTER para continuar")
    except ValueError:
        print("\nOpção Inválida. Digite 1, 2, 3 ou 4.\n")
        input("\nPressione ENTER para continuar")