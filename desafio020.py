velocidade = float(input('Digite a velocidade: '))

if velocidade>80.0:
    print('Multa de {} Reais'.format((velocidade-80.0)*7))
else:
    print('Nada')