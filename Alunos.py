import operator

def preencher_matriz(quantidade):
    alunos = list()
    for n in range(quantidade):
        alunos.append([input('Digite o nome do aluno: '), float(input('Digite a nota: '))])
    alunos.sort(key=operator.itemgetter(1))
    return alunos

def verificador_de_nota(matriz):
    alunos = list()
    if verificador_de_erros(matriz,alunos):
        return alunos
    else:
        if matriz[1][1] == matriz[2][1]:
            alunos.append(matriz[1])
            alunos.append(matriz[2])
        else:
            alunos.append(matriz[1])

        return alunos

def verificador_de_erros(matriz,alunos):
    if len(matriz)>=3:
        return False
    elif len(matriz)==1:
        print('Só existe 1 aluno')
        return True
    else:
        alunos.append(matriz[1])
        return True

quantidade_de_alunos = int(input('Digite a quantidade de alunos: '))

alunos = preencher_matriz(quantidade_de_alunos)

segunda_menor_nota = verificador_de_nota(alunos)

for n in segunda_menor_nota:
    print(n[0])