## Usuário entra com 10 números e exibe quantos são positivos, negativos ou zero.

nPositivo, nNegativo, nZero = [0,0,0]

for x in range (10):
    numero = int(input("Digite o número "+str(x)+": "))
    if numero > 0:
        nPositivo += 1
    elif numero <0:
        nNegativo += 1
    else:
        nZero +=1

print (f"\nNúmeros Positivos: "+ str(nPositivo))
print (f"Números Negativos: "+ str(nNegativo))
print (f"Números Zero: "+ str(nZero)+'\n')