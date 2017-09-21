matriz=[[" "," "," "],[" "," "," "],[" "," "," "]]
turno=True #Marcador de seleção de turno
l=0 #Input linha
c=0 #Input coluna
player1=" " #Nome do Jogador 1
player2=" " #Nome do Jogador 2
vitória=False #Marcador de vitória e fim do jogo
fimTurno=False

#==============CONTAGEM DE POSSIBILIDADES DE JOGADAS PELA IA============
contaposs1=0
contaposs2=0
contaposs3=0
contaposs4=0
contaposs5=0
contaposs6=0
contaposs7=0
contaposs8=0
#=======================================================================

modoJogo=False #Sigleplayer ou vs

import os
import random

def TelaJogo():
    global matriz
    os.system('cls')
    print('')
    for linha in matriz:
        print('|',end=" ")
        for coluna in linha:
            print('{:^3} |'.format(coluna), end=" ")
        print('\n'+'-'*19)

def inteligencia():
    global contaposs1, contaposs2, contaposs3, contaposs4, contaposs5, contaposs6, contaposs7, contaposs8
    global fimTurno
    fimTurno=False
    contaposs1 = 0
    contaposs2 = 0
    contaposs3 = 0
    contaposs4 = 0
    contaposs5 = 0
    contaposs6 = 0
    contaposs7 = 0
    contaposs8 = 0

    possibilidade1()
    possibilidade2()
    possibilidade3()
    possibilidade4()
    possibilidade5()
    possibilidade6()
    possibilidade7()
    possibilidade8()

    inteligencia_vitoria()
    if fimTurno==False:
        ameaça_derrota()
    if fimTurno==False:
        verifica_jogada()

def verifica_jogada():
    global contaposs1, contaposs2, contaposs3, contaposs4, contaposs5, contaposs6, contaposs7, contaposs8
    global fimTurno
    ref = 3
    if matriz[1][1]==" ":
        matriz[1][1]="O"
    else:
        while ref>0:
            if contaposs1==ref:
                if matriz[0][0]==" ":
                    matriz[0][0]="O"
                    fimTurno=True
                    break
            if contaposs2==ref:
                if matriz[0][2]==" ":
                    matriz[0][2]="O"
                    fimTurno = True
                    break
            if contaposs3==ref:
                if matriz[2][0]==" ":
                    matriz[2][0]="O"
                    fimTurno = True
                    break
            if contaposs4==ref:
                if matriz[2][2]==" ":
                    matriz[2][2]="O"
                    fimTurno = True
                    break
            if contaposs5==ref:
                if matriz[1][0]==" ":
                    matriz[1][0]="O"
                    fimTurno = True
                    break
            if contaposs6==ref:
                if matriz[0][1]==" ":
                    matriz[0][1]="O"
                    fimTurno = True
                    break
            if contaposs7==ref:
                if matriz[1][2]==" ":
                    matriz[1][2]="O"
                    fimTurno = True
                    break
            if contaposs8==ref:
                if matriz[2][1]==" ":
                    matriz[2][1]="O"
                    fimTurno = True
                    break
            ref-=1

def inteligencia_vitoria():
    global matriz, fimTurno

    for i in range(1,2):
# =========LINHA 01========================================================

        cont = 0
        for co in range(0, 3):
            if matriz[0][co] == "O":
                cont += 1
        if cont == 2:
            for co in range(0, 3):
                if matriz[0][co] == " ":
                    matriz[0][co] = "O"
                    fimTurno=True

        break

    # ========LINHA 02=========================================================
        cont = 0
        for co in range(0, 3):
            if matriz[1][co] == "O":
                cont += 1
        if cont == 2:
            for co in range(0, 3):
                if matriz[1][co] == " ":
                    matriz[1][co] = "O"
                    fimTurno = True

        break

    # ========LINHA 03=========================================================
        cont = 0
        for co in range(0, 3):
            if matriz[2][co] == "O":
                cont += 1
        if cont == 2:
            for co in range(0, 3):
                if matriz[2][co] == " ":
                    matriz[2][co] = "O"
                    fimTurno = True

        break

    # ========COLUNA 01========================================================
        cont = 0
        for li in range(0, 3):
            if matriz[li][0] == "O":
                cont += 1
        if cont == 2:
            for li in range(0, 3):
                if matriz[li][0] == " ":
                    matriz[li][0] = "O"
                    fimTurno = True

        break

    # ========COLUNA 02=========================================================
        cont = 0
        for li in range(0, 3):
            if matriz[li][1] == "O":
                cont += 1
        if cont == 2:
            for li in range(0, 3):
                if matriz[li][1] == " ":
                    matriz[li][1] = "O"
                    fimTurno = True

        break

    # ========COLUNA 03=========================================================
        cont = 0
        for li in range(0, 3):
            if matriz[li][2] == "O":
                cont += 1
        if cont == 2:
            for li in range(0, 3):
                if matriz[li][2] == " ":
                    matriz[li][2] = "O"
                    fimTurno = True

        break

    # ========DIAGONAL ESQUERDA=================================================
        cont = 0
        for r in range(0, 3):
            if matriz[r][r] == "O":
                cont += 1
        if cont == 2:
            for r in range(0, 3):
                if matriz[r][r] == " ":
                    matriz[r][r] = "O"
                    fimTurno = True

        break

    # =========DIAGONAL DIREITA=================================================
        cont = 0
        co = 2
        for r in range(0, 3):
            if matriz[r][co] == "O":
                cont += 1
            co -= 1
        if cont == 2:
            co = 2
            for r in range(0, 3):
                if matriz[r][co] == " ":
                    matriz[r][co] = "O"
                    fimTurno = True
                co -= 1
        break


def ameaça_derrota():
    global matriz, fimTurno
#=========LINHA 01========================================================
    cont=0
    for co in range(0,3):
        if matriz[0][co]=="X":
            cont+=1
    if cont==2:
        for co in range(0,3):
            if matriz[0][co]==" ":
                matriz[0][co]="O"
                fimTurno = True
#========LINHA 02=========================================================
    cont=0
    for co in range(0,3):
        if matriz[1][co]=="X":
            cont+=1
    if cont==2:
        for co in range(0,3):
            if matriz[1][co]==" ":
                matriz[1][co]="O"
                fimTurno = True
#========LINHA 03=========================================================
    cont=0
    for co in range(0,3):
        if matriz[2][co]=="X":
            cont+=1
    if cont==2:
        for co in range(0,3):
            if matriz[2][co]==" ":
                matriz[2][co]="O"
                fimTurno = True
#========COLUNA 01========================================================
    cont = 0
    for li in range(0, 3):
        if matriz[li][0]=="X":
            cont += 1
    if cont == 2:
        for li in range(0, 3):
            if matriz[li][0] == " ":
                matriz[li][0] = "O"
                fimTurno = True
#========COLUNA 02=========================================================
    cont = 0
    for li in range(0, 3):
        if matriz[li][1]=="X":
            cont += 1
    if cont == 2:
        for li in range(0, 3):
            if matriz[li][1] == " ":
                matriz[li][1] = "O"
                fimTurno = True
#========COLUNA 03=========================================================
    cont = 0
    for li in range(0, 3):
        if matriz[li][2]=="X":
            cont += 1
    if cont == 2:
        for li in range(0, 3):
            if matriz[li][2] == " ":
                matriz[li][2] = "O"
                fimTurno = True
#========DIAGONAL ESQUERDA=================================================
    cont = 0
    for r in range(0, 3):
        if matriz[r][r]=="X":
            cont += 1
    if cont == 2:
        for r in range(0, 3):
            if matriz[r][r] == " ":
                matriz[r][r] = "O"
                fimTurno = True
#=========DIAGONAL DIREITA=================================================
    cont = 0
    co=2
    for r in range(0,3):
        if matriz[r][co]=="X":
            cont += 1
        co -=1

    if cont == 2:
        co = 2
        for r in range(0, 3):
            if matriz[r][co]==" ":
                matriz[r][co] = "O"
                fimTurno = True
            co-=1

def possibilidade1(): #matriz[0][0]
    global matriz, contaposs1
    if (matriz[0][0] == " " or matriz[0][0] == "O") and (matriz[1][1] == " " or matriz[1][1] == "O") and (matriz[2][2] == " " or matriz[2][2] == "O"):
        contaposs1+=1
    if (matriz[0][0] == " " or matriz[0][0] == "O") and (matriz[0][1] == " " or matriz[0][1] == "O") and (matriz[0][2] == " " or matriz[0][2] == "O"):
        contaposs1+=1
    if (matriz[0][0] == " " or matriz[0][0] == "O") and (matriz[1][0] == " " or matriz[1][0] == "O") and (matriz[2][0] == " " or matriz[2][0] == "O"):
        contaposs1+=1

def possibilidade2(): #matriz[0][2]
    global matriz, contaposs2
    if (matriz[0][2] == " " or matriz[0][2] == "O") and (matriz[1][1] == " " or matriz[1][1] == "O") and (matriz[2][0] == " " or matriz[2][0] == "O"):
        contaposs2+=1
    if (matriz[0][0] == " " or matriz[0][0] == "O") and (matriz[0][1] == " " or matriz[0][1] == "O") and (matriz[0][2] == " " or matriz[0][2] == "O"):
        contaposs2+=1
    if (matriz[0][2] == " " or matriz[0][2] == "O") and (matriz[1][2] == " " or matriz[1][2] == "O") and (matriz[2][2] == " " or matriz[2][2] == "O"):
        contaposs2+=1

def possibilidade3(): #matriz[2][0]
    global matriz, contaposs3
    if (matriz[0][2] == " " or matriz[0][2] == "O") and (matriz[1][1] == " " or matriz[1][1] == "O") and (matriz[2][0] == " " or matriz[2][0] == "O"):
        contaposs3+=1
    if (matriz[2][0] == " " or matriz[2][0] == "O") and (matriz[1][0] == " " or matriz[1][0] == "O") and (matriz[0][0] == " " or matriz[0][0] == "O"):
        contaposs3+=1
    if (matriz[2][0] == " " or matriz[2][0] == "O") and (matriz[2][1] == " " or matriz[2][1] == "O") and (matriz[2][2] == " " or matriz[2][2] == "O"):
        contaposs3+=1

def possibilidade4(): #matriz[2][2]
    global matriz, contaposs4
    if (matriz[0][0] == " " or matriz[0][0] == "O") and (matriz[1][1] == " " or matriz[1][1] == "O") and (matriz[2][2] == " " or matriz[2][2] == "O"):
        contaposs4+=1
    if (matriz[0][2] == " " or matriz[0][2] == "O") and (matriz[1][2] == " " or matriz[1][2] == "O") and (matriz[2][2] == " " or matriz[2][2] == "O"):
        contaposs4+=1
    if (matriz[2][0] == " " or matriz[2][0] == "O") and (matriz[2][1] == " " or matriz[2][1] == "O") and (matriz[2][2] == " " or matriz[2][2] == "O"):
        contaposs4+=1

def possibilidade5(): #matriz[1][0]
    global matriz, contaposs5
    if (matriz[0][0] == " " or matriz[0][0] == "O") and (matriz[1][0] == " " or matriz[0][1] == "O") and (matriz[2][0] == " " or matriz[2][0] == "O"):
        contaposs5+=1
    if (matriz[1][0] == " " or matriz[1][0] == "O") and (matriz[1][1] == " " or matriz[1][1] == "O") and (matriz[1][2] == " " or matriz[1][2] == "O"):
        contaposs5+=1

def possibilidade6(): #matriz[0][1]
    global matriz, contaposs6
    if (matriz[0][0] == " " or matriz[0][0] == "O") and (matriz[0][1] == " " or matriz[0][1] == "O") and (matriz[0][2] == " " or matriz[0][2] == "O"):
        contaposs6+=1
    if (matriz[0][1] == " " or matriz[0][1] == "O") and (matriz[1][1] == " " or matriz[1][1] == "O") and (matriz[1][0] == " " or matriz[1][0] == "O"):
        contaposs6+=1

def possibilidade7(): #matriz[1][2]
    global matriz, contaposs7
    if (matriz[1][0] == " " or matriz[1][0] == "O") and (matriz[1][1] == " " or matriz[1][1] == "O") and (matriz[1][2] == " " or matriz[1][2] == "O"):
        contaposs7+=1
    if (matriz[0][2] == " " or matriz[0][2] == "O") and (matriz[1][2] == " " or matriz[1][2] == "O") and (matriz[2][2] == " " or matriz[2][2] == "O"):
        contaposs7+=1

def possibilidade8(): #matriz[2][1]
    global matriz, contaposs8
    if (matriz[2][0] == " " or matriz[2][0] == "O") and (matriz[2][1] == " " or matriz[2][1] == "O") and (matriz[2][2] == " " or matriz[2][2] == "O"):
        contaposs8+=1
    if (matriz[0][1] == " " or matriz[0][1] == "O") and (matriz[1][1] == " " or matriz[1][1] == "O") and (matriz[1][0] == " " or matriz[1][0] == "O"):
        contaposs8+=1

def definir_player():
    global modoJogo
    pl = [True, False]
    turno = random.choice(pl)
    for i in range(1, 10):
        if turno == True:
            player_1()
            TelaJogo()
            turno = not (turno)
        else:
            if modoJogo==True:
                inteligencia()
                TelaJogo()
                turno = not (turno)
            else:
                player_2()
                TelaJogo()
                turno = not(turno)



def player_1():
    global matriz, l, c, player1
    print('Turno do jogador 1')
    validar_jogada()
    matriz[l-1][c-1]='X'

def player_2():
    global matriz, l, c, player2
    print('Turno do jogador 2')
    validar_jogada()
    matriz[l - 1][c - 1] = 'O'

def validar_jogada():
    global l,c
    while True:
        try:
            l = int(input('Digite a linha: '))
            c = int(input('Digite a coluna: '))
            break
        except ValueError:
            print('JOGADA NÃO VÁLIDA! SOMENTE NÚMEROS INTEIROS DE 1 A 3 SÃO ACEITOS')
    while (l < 1 or l > 3) or (c < 1 or c > 3):
        print('SOMENTE NÚMEROS INTEIROS DE 1 A 3 SÃO VÁLIDOS')
        l = int(input('Digite novamente a linha: '))
        c = int(input('Digite novamente a coluna: '))
    while matriz[l-1][c-1] != " ":
        print('JOGADA NÃO VÁLIDA!')
        l = int(input('Digite novamente a linha: '))
        c = int(input('Digite novamente a coluna: '))

def modo_de_jogo():
    global modoJogo
    modo=int(input('Digite (1) para singleplayer ou (2) para modo vs: '))
    if modo==1:
        modoJogo=True
    if modo==2:
        modoJogo=False

def main():
    TelaJogo()
    modo_de_jogo()
    definir_player()

main()