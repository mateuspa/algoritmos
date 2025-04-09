## O computador escolhe um número aleatório de 1 a 10, e o usuário tem 3 tentativas para adivinhar. Dê dicas se o número é maior ou menor.

import random

numero = random.randint(0,2)
print (f"Esse é um jogo para descobrir um número entre 0 a 10. Você tem 3 tentativas para acertar o número\n")

for x in range(3):
    tentativa = int(input ("Digite um número: "))
    if numero > tentativa:
        print ("Você escolheu um número menor que o número secreto\n")
    elif numero < tentativa:
        print ("Você escolheu um número maior que o número secreto\n")
    else:
        print ("Você acertou!!! Parabéns!!! \n")
        break

print(f"Número correto é: {numero}\n")