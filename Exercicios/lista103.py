book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string
t = book1.split("by")
print(t[0])

t2 = book2.split("by")
print(book2.split("by")[0])

t3 = book3.split("by Nassim")
print(book3.split("by")[0])

# 2) Salve o titulo de cada livro em uma variável

titulo1 = t[0]
titulo2 = t2[0]
titulo3 = t3[0]

# 3) Quantos caracteres cada título tem?
# pra n contar os espacos
print(sum(len(x) for x in titulo1.split()))
print(sum(len(x) for x in titulo2.split()))
print(sum(len(x) for x in titulo3.split()))


# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}

b = t[1]
autor, ano = b.split(",")
printzao = '{0}, {1}, {2}'.format(titulo1, autor, ano)
print(printzao)

b2 = t2[1]
autor2, ano2 = b2.split(",")
printzao2 = '{0}, {1}, {2}'.format(titulo2, autor2, ano2)
print(printzao2)

b3 = t3[1]
autor3, ano3 = b3.split(",")
printzao3 = '{0}, {1}, {2}'.format(titulo3, autor3, ano3)
print(printzao3)

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

pali1 = palindrome_one[::-1]
if palindrome_one == pali1:
    print("é")
else:
    print("n eh")

palindrome_two = palindrome_two.lower().replace(' ', '')
pali2 = palindrome_two[::-1]
if palindrome_two == pali2:
    print("é")
else:
    print("n eh")

palindrome_three = palindrome_three.lower().replace(' ', '')
pali3 = palindrome_three[::-1]
if palindrome_three == pali3:
    print("é")
else:
    print("n eh")

palindrome_four = palindrome_four.lower().replace(' ', '')
pali4 = palindrome_four[::-1]
if palindrome_three == pali4:
    print("é")
else:
    print("n eh")
