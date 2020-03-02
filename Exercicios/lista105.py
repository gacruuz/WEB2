# Usando a lista: ['a','b','c']

lista = ['a', 'b', 'c']

# 1) Faca um loop para retornar: ['A','B','C']
# n eentendi oq era pra printar kkk

tam = len(lista)
for x in range(tam):
    print(lista)

for x in range(tam):
    print(lista[x])

lista2 = [0, 1, 3, 4, 5]
# 2) Faca um loop para retornar a soma de todos os elementos da listas

tam2 = len(lista2)
soma = 0
for x2 in range(tam2):
    soma = soma + lista2[x2]

print(soma)

# 3) Faca um loop para retornar apenas os numeros impares

for t in range(tam2):
    if lista2[t] % 2 != 0:
        print(lista2[t])

# 4) Conte quantas palavras de tamanho >= 5 existe nessa string
string = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
stringteste = 'faustao ovo faustinho cabe'

help = stringteste.split(" ")
tamanhostring = len(help)

cont = 0

for x4 in range(tamanhostring):
    if len(help[x4]) >= 5:
        cont = cont + 1

print(cont)

# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100

lista5 = [i * 3 for i in range(100) if (i*3) <= 100]
print(lista5)