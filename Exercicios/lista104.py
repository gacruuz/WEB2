# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e
# sua ordem devem ser o mesmo. Retorne True ou False.

list1 = ['a', 'b', 'c', 'z']
list2 = ['a', 'b', 'c']

def massa(lista1, lista2):
    if ( lista1 == lista2):
        return True
    else:
        return False

print(massa(list1, list2))

# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.
# Retorne True ou False.

ae = "ovo"
ae2 = "faustao"

def test(ae):
    bola1 = ae.lower().replace('','')

    if bola1 == bola1[::-1]:
        return True
    else:
        return False

print(test(ae))



