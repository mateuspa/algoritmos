## implementando loops
print("")
inicio = int(input("Digite o valor do início: "))
fim = int(input("Digite o valor do fim: "))
print("")
for i in range (inicio,fim,1):

    if i%2 ==0:
        print(f"{i} é PAR")
    else:
        print(f"{i} é IMPAR")

print("")