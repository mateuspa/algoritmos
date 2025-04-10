# simulador caixa
import time

def main():
    saldo = float(1000)

    print("")

    operation = str(input("Digite s para saque, d para depósito. Qualquer outra letra não vai funcionar!"))
    
    if operation == "s" or operation == "S":
        print ("Operação de Saque")
        print("")
        if saldo > 0:
            saque = float(input("Qual o valor do saque? R$ "))
            if saque <= saldo:
                print (f"Saque de R$: {saque:,.2f}")
                saldo = saldo-saque
                print (f"Saldo remanescente: R$ {saldo:,.2f}")
            else:
                print ("Saldo Insuficiente")
        else:
            print("Saldo Zerado")
    elif operation == "d" or operation == "D":
        print ("Operação de Depósito")
        print("")
        print (f"Saldo atual: R$ {saldo:,.2f}")
        print("")
        deposito = float(input("Qual o valor do deposito? R$ "))
        print (f"Depósito de R$: {deposito:,.2f}")
        saldo = saldo+deposito
        print (f"Saldo atualizado: R$ {saldo:,.2f}")
    else:
        print("Operação Inválida. Tente novamente...")
   
    print("")
    time.sleep(2)
main()