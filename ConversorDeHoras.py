class Horario(object):
    def conversor_am(self, horas):
        if horas[0]=='12':
            horas[0] = '00'

        horas[2] = horas[2][0:2]

    def conversor_pm(self, horas):

        if horas[0] == '12':

            horas[0] = '00'

        else:
            valor = int(horas[0]) +12
            horas[0] = valor

        horas[2] = horas[2][0:2]

hora = input("Digite no formato HH:MM:SSAM\n").split(':')

h = Horario()

if hora[2][-2].lower() == 'a':
    h.conversor_am(hora)
else:
    h.conversor_pm(hora)

print('{}:{}:{}'.format(hora[0], hora[1], hora[2]))
