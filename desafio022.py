distancia = float(input('Distância: '))

if distancia<=200:
    passagem = 0.5*distancia
else:
    passagem = 0.45*distancia

print(passagem)