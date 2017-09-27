nome = input('Digite o seu nome completo: ').strip()
#print(nome.upper())
#print(nome.lower())
#print(len(nome.strip()) - nome.count(' '))
#print(len(nome.split(' ')[0]))

lista = nome.split(' ')

print('{}'.format(lista[0]))
print(('{}'.format(lista[-1])))
