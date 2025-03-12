"""
# comparador de dois números

n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))


if n1 > n2:
    print (n1," é maior que ",n2)
elif n1 < n2:
    print (n1," é menor que ",n2)
else:
    print (n1, "é igual ", n2)


# verificador de faixa etária

def main():
    print("")

    n1 = int(input("Digite a sua idade é anos inteiros: "))

    if n1 >= 65:
        print ("Idoso")
    elif n1 >= 18:
        print("Adulto")
    elif n1 >= 13:
        print("Adolescente")
    else:
        print ("Criança")
main()


# calculadora com operações simples

print("")

def main():
    operation = str(input("Digite A para Adição, S para Subtação, M para Multiplicação e D para Divisão. Qualquer outra letra não vai funcionar!"))
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))


    if operation == "A" or operation == "a":
        print ("Adição")
        print (n1 - n2)
    elif operation == "S" or operation == "s":
        print ("Subtração")
        print(n1 - n2)
    elif operation == "M" or operation == "m":
        print ("Multiplicação")
        print(n1 * n2)
    elif operation == "D" or operation == "d":
        print ("Divisão")
        print(n1 / n2)
    else:
        print ("Nenhuma operação realizada!! ")

main()


# descobrir se é par

print ("")
n1 = int(input("Digite um número: "))

if n1 % 2 == 0:
    print ("é par")
    
else:
    print ("é impar")


# verificador de faixa de notas

import time

def main():
    print("")

    n1 = float(input("Digite a nota: "))

    if n1 >= 90:
        print ("A")
    elif n1 >= 80:
        print("B")
    elif n1 >= 70:
        print("C")
    elif n1 >= 60:
        print("D")
    else:
        print ("F")
    time.sleep(2)
main()
"""


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