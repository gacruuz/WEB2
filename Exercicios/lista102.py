weekdays = ['mon','tues','wed','thurs','fri']
list = ['a', 1, 3.14159265359]

# Como selecionar 'wed' pelo indice?
print(weekdays[2])

# Como verificar o tipo de 'mon'?
print(type (weekdays[0]))

# Como separar 'wed' até 'fri'?
print(weekdays[2:5])

# Quais as maneiras de selecionar 'fri' por indice?
print(weekdays[4])
print(weekdays[-1])

# Qual eh o tamanho dos dias e days_list?
print(len(weekdays))

# Como inverter a ordem dos dias?
print(weekdays[::-1])

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
list.insert(1, 'zero')
print(list)

# Como limpar list?
#list.clear()
#print(list)

# Como deletar list?
#del(list)

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
ultimo = list[len(list)-1]
list.remove(ultimo)
print(list)


