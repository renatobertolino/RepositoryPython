from random import randint
from time import sleep

computador = randint(0,5)
print('-=-' * 10)
print('Otário')
print('-=-' * 10)

numero = int(input('Digite o número: '))

print('PROCESSANDO...')
sleep(2)

if numero == computador:
    print('Ganhou')
else:
    print('Perdeu')