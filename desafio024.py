x = int(input('Primeiro valor:'))
y = int(input('Segundo valor:'))
z = int(input('Terceiro valor:'))

menor = x

if y<x and y<z:
    menor = y
elif z<x and z<y:
    menor = z

print(menor)
maior = x

if y>x and y>z:
    maior = y
elif z>x and z>y:
    maior = z

print(maior)