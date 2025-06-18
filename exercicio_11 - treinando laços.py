quantidade = int(input("Quantos numeros você quer testar? "))
acumulador_par = 0
num_par = 0
media_par = 0
acumulador_impar = 0
num_impar = 0
media_impar = 0

for i in range (quantidade):
    if (i%2 == 0):
        print (f"{i} é par")
        acumulador_par += i
        num_par+=1
    else:
        print (f"{i} é ímpar")
        acumulador_impar += i
        num_impar+=1

media_par = acumulador_par/num_par
media_impar = acumulador_impar/num_impar
print (f"A média de numeros pares é {media_par}")
print (f"A média de numeros ímpares é {media_impar}")

