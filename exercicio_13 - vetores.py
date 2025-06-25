
# Exemplo de vetor com números inteiros
numeros = [11, 22, 33, 44, 55, 66, 77]

# Lista com diferentes tipos de dados
mistura = [77, "Olá", True, 3.1415,"Mateus Prince"]

# Acessando elementos
frutas = ["maçã", "banana", "uva", "laranja"]
print(frutas[0])  # maçã
print(frutas[2])  # uva
print(frutas[-1]) # laranja (último elemento)

# Alterando elementos
frutas[1] = "pera"
print(frutas)

# Adicionando elementos
frutas.append("melancia")
print(frutas)

frutas.insert(2, "abacaxi")
print(frutas)

# Removendo elementos
frutas.remove("uva")
print(frutas)

frutas.pop(0)
print(frutas)

# Percorrendo listas com for
for numero in numeros:
    print(numero * 2)

# Tamanho da lista
print(len(numeros),len(mistura),len(frutas))

#Exercícios práticos
alunos = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
for nome in alunos:
    print(nome, "está presente?")

print("Primeiro:", numeros[0])
print("Último:", numeros[-1])
print("Soma:", sum(numeros))

numeros = []
for i in range(5):
    valor = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

for n in numeros:
    print(f"{n}")