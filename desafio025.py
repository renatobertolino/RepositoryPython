salario = float(input('Digite o salário: '))

if salario>1250.0:
    salario = salario + (salario/100*10)
else:
    salario = salario + (salario/100*15)

print(salario)