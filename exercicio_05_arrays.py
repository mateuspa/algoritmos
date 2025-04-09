## Peça ao usuário 3 números e exiba quais são positivos, negativos ou zero.
import array

y = []

for x in range (10):
    temp = int(input ("Digite o número "+ str(x) +": "))
    y.append (temp)

print (f"\nVocê digitou: ")

for x in range (10):
    ##print (f"Você digitou: {y[x]}")
    if y[x] > 0:
        print (f"{y[x]} é positivo")
    elif y[x] < 0:
        print (f"{y[x]} é negativo")
    else:
        print (f"{y[x]} é zero")

print("")