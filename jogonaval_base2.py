import random

matrizjogador = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

matrizmaquina = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

matrizjogador2 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

matrizmaquina2 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

##modo de jogo clássico

##essa função define em quais posições o jogador colocou os barcos
def escolhaBarcoJogador():
    barcosJogador = 0
    print("Escolha 5 posições para colocar seus barcos")
    while barcosJogador < 5:
        posicaolinha = int(input("Linha: "))
        if posicaolinha < 0 or posicaolinha > 4:
            print("Posição inválida")
            continue

        posicaocoluna = int(input("Coluna: "))
        if posicaocoluna < 0 or posicaocoluna > 9:
            print("Posição inválida")
            continue

        if matrizjogador[posicaolinha][posicaocoluna] == 1:
            print("Um barco ja está locado nessa posição")
            continue
             
        matrizjogador[posicaolinha][posicaocoluna] = 1
        barcosJogador += 1

##essa função define em quais posições a maquina colocou os barcos
def escolhaBarcoMaquina():
    barcosMaquina = 0
    while barcosMaquina < 5:
        posicaolinhaMaquina = random.randint(0,4)
        posicaocolunaMaquina = random.randint(0,9)
        if matrizmaquina[posicaolinhaMaquina][posicaocolunaMaquina] == 1:
            continue

        matrizmaquina[posicaolinhaMaquina][posicaocolunaMaquina] = 1
        barcosMaquina += 1

##modo de jogo desafio

##essa funcao define em quais posicoes o player colocou as 5 frotas
def escolhaFrotaJogador():

    frotaJogadorPA = 0
    frotaJogadorNV = 0
    frotaJogadorCT = 0
    frotaJogadorSU = 0
    frotaJogadorDE = 0

    while frotaJogadorPA < 1:

        escolhaHVPA = int(input("Escolha uma posicao para o seu Porta-Aviões (5 casas).\nDeseja coloca-lo:\nHorizontal - 0\nVertical - 1\n"))
        
        if escolhaHVPA == 0:
            linhaEscolhaPA = int(input("Linha: "))
            colunaEscolhaPA = int(input("Coluna: "))

            if colunaEscolhaPA + 4 < 10:
                livre = True
            
                for i in range(5):
                    if matrizjogador[linhaEscolhaPA][colunaEscolhaPA + i] != 0:
                        livre = False

                if livre:
                    for i in range(5):
                        matrizjogador[linhaEscolhaPA][colunaEscolhaPA + i] = 5
                    mostrarMatrizJogador()    
                    print("Porta-aviões posicionado!")
                    frotaJogadorPA = 1

                else:
                    print("Já existe uma frota nessa posição.")
                    mostrarMatrizJogador()

            else:
                print("O Porta-Aviões não cabe nessa posição.")
                mostrarMatrizJogador()
        
        elif escolhaHVPA == 1:
            linhaEscolhaPA = 0
            colunaEscolhaPA = int(input("Coluna: "))

            if linhaEscolhaPA + 4 < 5:
                livre = True

                for i in range(5):
                    if matrizjogador[linhaEscolhaPA + i][colunaEscolhaPA] != 0:
                        livre = False

                if livre:
                    for i in range(5):
                        matrizjogador[linhaEscolhaPA + i][colunaEscolhaPA] = 5
                    mostrarMatrizJogador()
                    print("Porta-Aviões posicionado!")
                    frotaJogadorPA = 1

                else:
                    print("Já existe uma frota nessa posição.")
                    mostrarMatrizJogador()
            else:
                print("O Porta-Aviões não cabe nessa posição.")
                mostrarMatrizJogador()

        else:
            print("Resposta invalida.")

    while frotaJogadorNV < 1:
    
        escolhaHVNV = int(input("Escolha uma posicao para o seu Navio-Tanque (4 casas).\nDeseja coloca-lo:\nHorizontal - 0\nVertical - 1\n"))
        
        if escolhaHVNV == 0:
            linhaEscolhaNV = int(input("Linha: "))
            colunaEscolhaNV = int(input("Coluna: "))

            if colunaEscolhaNV + 3 < 10:
                livre = True
            
                for i in range(4):
                    if matrizjogador[linhaEscolhaNV][colunaEscolhaNV + i] != 0:
                        livre = False

                if livre:
                    for i in range(4):
                        matrizjogador[linhaEscolhaNV][colunaEscolhaNV + i] = 4
                    mostrarMatrizJogador()    
                    print("Navio-Tanque posicionado!")
                    frotaJogadorNV = 1

                else:
                    print("Já existe uma frota nessa posição.")
                    mostrarMatrizJogador()

            else:
                print("O Navio-Tanque não cabe nessa posição.")
                mostrarMatrizJogador()
        
        elif escolhaHVNV == 1:
            linhaEscolhaNV = int(input("Linha: "))
            colunaEscolhaNV = int(input("Coluna: "))

            if linhaEscolhaNV + 3 < 5:
                livre = True

                for i in range(4):
                    if matrizjogador[linhaEscolhaNV + i][colunaEscolhaNV] != 0:
                        livre = False

                if livre:
                    for i in range(4):
                        matrizjogador[linhaEscolhaNV + i][colunaEscolhaNV] = 4
                    mostrarMatrizJogador()
                    print("Navio-Tanque posicionado!")
                    frotaJogadorNV = 1

                else:
                    print("Já existe uma frota nessa posição.")
                    mostrarMatrizJogador()
            else:
                print("O Navio-Tanque não cabe nessa posição.")
                mostrarMatrizJogador()

        else:
            print("Resposta invalida.")
                
    while frotaJogadorCT < 1:
        
            escolhaHVCT = int(input("Escolha uma posicao para o seu Contratorpedeiro (3 casas).\nDeseja coloca-lo:\nHorizontal - 0\nVertical - 1\n"))
            
            if escolhaHVCT == 0:
                linhaEscolhaCT = int(input("Linha: "))
                colunaEscolhaCT = int(input("Coluna: "))

                if colunaEscolhaCT + 2 < 10:
                    livre = True
                
                    for i in range(3):
                        if matrizjogador[linhaEscolhaCT][colunaEscolhaCT + i] != 0:
                            livre = False

                    if livre:
                        for i in range(3):
                            matrizjogador[linhaEscolhaCT][colunaEscolhaCT + i] = 3
                        mostrarMatrizJogador()    
                        print("Contratorpedeiro posicionado!")
                        frotaJogadorCT = 1

                    else:
                        print("Já existe uma frota nessa posição.")
                        mostrarMatrizJogador()

                else:
                    print("O Contratorpedeiro não cabe nessa posição.")
                    mostrarMatrizJogador()
            
            elif escolhaHVCT == 1:
                linhaEscolhaCT = int(input("Linha: "))
                colunaEscolhaCT = int(input("Coluna: "))

                if linhaEscolhaCT + 2 < 5:
                    livre = True

                    for i in range(3):
                        if matrizjogador[linhaEscolhaCT + i][colunaEscolhaCT] != 0:
                            livre = False

                    if livre:
                        for i in range(3):
                            matrizjogador[linhaEscolhaCT + i][colunaEscolhaCT] = 3
                        mostrarMatrizJogador()
                        print("Contratorpedeiro posicionado!")
                        frotaJogadorCT = 1

                    else:
                        print("Já existe uma frota nessa posição.")
                        mostrarMatrizJogador()
                else:
                    print("O Contratorpedeiro não cabe nessa posição.")
                    mostrarMatrizJogador()

            else:
                print("Resposta invalida.")

    while frotaJogadorSU < 1:
        
            escolhaHVSU = int(input("Escolha uma posicao para o seu Submarino (2 casas).\nDeseja coloca-lo:\nHorizontal - 0\nVertical - 1\n"))
            
            if escolhaHVSU == 0:
                linhaEscolhaSU = int(input("Linha: "))
                colunaEscolhaSU = int(input("Coluna: "))

                if colunaEscolhaSU + 1 < 10:
                    livre = True
                
                    for i in range(2):
                        if matrizjogador[linhaEscolhaSU][colunaEscolhaSU + i] != 0:
                            livre = False

                    if livre:
                        for i in range(2):
                            matrizjogador[linhaEscolhaSU][colunaEscolhaSU + i] = 2
                        mostrarMatrizJogador()    
                        print("Submarino posicionado!")
                        frotaJogadorSU = 1

                    else:
                        print("Já existe uma frota nessa posição.")
                        mostrarMatrizJogador()

                else:
                    print("O Submarino não cabe nessa posição.")
                    mostrarMatrizJogador()
            
            elif escolhaHVSU == 1:
                linhaEscolhaSU = int(input("Linha: "))
                colunaEscolhaSU = int(input("Coluna: "))

                if linhaEscolhaSU + 1 < 5:
                    livre = True

                    for i in range(2):
                        if matrizjogador[linhaEscolhaSU + i][colunaEscolhaSU] != 0:
                            livre = False

                    if livre:
                        for i in range(2):
                            matrizjogador[linhaEscolhaSU + i][colunaEscolhaSU] = 2
                        mostrarMatrizJogador()
                        print("Submarino posicionado!")
                        frotaJogadorSU = 1

                    else:
                        print("Já existe uma frota nessa posição.")
                        mostrarMatrizJogador()
                else:
                    print("O Submarino não cabe nessa posição.")
                    mostrarMatrizJogador()

            else:
                print("Resposta invalida.")

    while frotaJogadorDE < 1:
        
        linhaEscolhaDE = int(input("Escolha uma posicao para o seu Destroyer (1 casa).\nLinha: "))
        if linhaEscolhaDE < 0 or linhaEscolhaDE > 4:
            print("Posição inválida")
            continue

        colunaEscolhaDE = int(input("Coluna: "))
        if colunaEscolhaDE < 0 or colunaEscolhaDE > 9:
            print("Posição inválida")
            continue

        if matrizjogador[linhaEscolhaDE][colunaEscolhaDE] != 0:
            print("Uma frota ja esta nessa posição.")
            continue

        matrizjogador[linhaEscolhaDE][colunaEscolhaDE] = 1
        mostrarMatrizJogador()
        frotaJogadorDE = 1

##essa funcao define em quais posicoes a maquina colocou as 5 frotas                 
def escolhaFrotaMaquina():  

    frotaMaquinaPA = 0
    frotaMaquinaNV = 0
    frotaMaquinaCT = 0
    frotaMaquinaSU = 0
    frotaMaquinaDE = 0

    while frotaMaquinaPA < 1:

        escolhaHPVA = random.randint(0,1)

        if escolhaHPVA == 0:
            linhaEscolhaPA = random.randint(0,4)
            colunaEscolhaPA = random.randint(0,5)

            if colunaEscolhaPA + 4 < 10:
                livre = True
            
                for i in range(5):
                    if matrizmaquina[linhaEscolhaPA][colunaEscolhaPA + i] != 0:
                        livre = False

                if livre:
                    for i in range(5):
                        matrizmaquina[linhaEscolhaPA][colunaEscolhaPA + i] = 5
                    frotaMaquinaPA = 1                                                            
        
        elif escolhaHPVA == 1:
            linhaEscolhaPA = 0
            colunaEscolhaPA = random.randint(0,9)
            if linhaEscolhaPA + 4 < 5:
                livre = True

                for i in range(5):
                    if matrizmaquina[linhaEscolhaPA + i][colunaEscolhaPA] != 0:
                        livre = False

                if livre:
                    for i in range(5):
                        matrizmaquina[linhaEscolhaPA + i][colunaEscolhaPA] = 5
                    frotaMaquinaPA = 1

    while frotaMaquinaNV < 1:

        escolhaHPVA = random.randint(0,1)

        if escolhaHPVA == 0:
            linhaEscolhaNV = random.randint(0,4)
            colunaEscolhaNV = random.randint(0,6)

            if colunaEscolhaNV + 3 < 10:
                livre = True
            
                for i in range(4):
                    if matrizmaquina[linhaEscolhaNV][colunaEscolhaNV + i] != 0:
                        livre = False

                if livre:
                    for i in range(4):
                        matrizmaquina[linhaEscolhaNV][colunaEscolhaNV + i] = 4
                    frotaMaquinaNV = 1                                                            
        
        elif escolhaHPVA == 1:
            linhaEscolhaNV = random.randint(0,1)
            colunaEscolhaNV = random.randint(0,9)
            if linhaEscolhaNV + 3 < 5:
                livre = True

                for i in range(4):
                    if matrizmaquina[linhaEscolhaNV + i][colunaEscolhaNV] != 0:
                        livre = False

                if livre:
                    for i in range(4):
                        matrizmaquina[linhaEscolhaNV + i][colunaEscolhaNV] = 4
                    frotaMaquinaNV = 1

    while frotaMaquinaCT < 1:

        escolhaHPVA = random.randint(0,1)

        if escolhaHPVA == 0:
            linhaEscolhaCT = random.randint(0,4)
            colunaEscolhaCT = random.randint(0,7)

            if colunaEscolhaCT + 2 < 10:
                livre = True
            
                for i in range(3):
                    if matrizmaquina[linhaEscolhaCT][colunaEscolhaCT + i] != 0:
                        livre = False

                if livre:
                    for i in range(3):
                        matrizmaquina[linhaEscolhaCT][colunaEscolhaCT + i] = 3
                    frotaMaquinaCT = 1                                                            
        
        elif escolhaHPVA == 1:
            linhaEscolhaCT = random.randint(0,2)
            colunaEscolhaCT = random.randint(0,9)
            if linhaEscolhaCT + 2 < 5:
                livre = True

                for i in range(3):
                    if matrizmaquina[linhaEscolhaCT + i][colunaEscolhaCT] != 0:
                        livre = False

                if livre:
                    for i in range(3):
                        matrizmaquina[linhaEscolhaCT + i][colunaEscolhaCT] = 3
                    frotaMaquinaCT = 1

    while frotaMaquinaSU < 1:

        escolhaHPVA = random.randint(0,1)

        if escolhaHPVA == 0:
            linhaEscolhaSU = random.randint(0,4)
            colunaEscolhaSU = random.randint(0,8)

            if colunaEscolhaSU + 1 < 10:
                livre = True
            
                for i in range(2):
                    if matrizmaquina[linhaEscolhaSU][colunaEscolhaSU + i] != 0:
                        livre = False

                if livre:
                    for i in range(2):
                        matrizmaquina[linhaEscolhaSU][colunaEscolhaSU + i] = 2
                    frotaMaquinaSU = 1                                                            
        
        elif escolhaHPVA == 1:
            linhaEscolhaSU = random.randint(0,3)
            colunaEscolhaSU = random.randint(0,9)
            if linhaEscolhaSU + 1 < 5:
                livre = True

                for i in range(2):
                    if matrizmaquina[linhaEscolhaSU + i][colunaEscolhaSU] != 0:
                        livre = False

                if livre:
                    for i in range(2):
                        matrizmaquina[linhaEscolhaSU + i][colunaEscolhaSU] = 2
                    frotaMaquinaSU = 1

    while frotaMaquinaDE < 1:
        linhaEscolhaDE = random.randint(0,4)
        colunaEscolhaDE = random.randint(0,9)
        if matrizmaquina[linhaEscolhaDE][colunaEscolhaDE] != 0:
            continue

        matrizmaquina[linhaEscolhaDE][colunaEscolhaDE] = 1
        frotaMaquinaDE = 1

##gameplay

##essa função é a gameplay do jogo
def jogo():
    while (True):

        ##jogada do jogador
        print("Escolha uma posição para atacar!")

        ataquelinhaJogador = int(input("Linha: "))
        if ataquelinhaJogador < 0 or ataquelinhaJogador > 4:
            print("Ataque inválido")
            continue

        ataquecolunaJogador = int(input("Coluna: "))
        if ataquecolunaJogador < 0 or ataquecolunaJogador > 9:
            print("Ataque inválido")
            continue

        if matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] == 'X' or matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] == 'N':
            print("Você já atacou essa posição!")
            continue

        if matrizmaquina[ataquelinhaJogador][ataquecolunaJogador] != 0:
            print("Acertou!")
            matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] = 'X'
            matrizmaquina[ataquelinhaJogador][ataquecolunaJogador] = 0

        else:
            print("Errou")
            matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] = 'N'

        for linha in matrizjogador2:
            print(linha)

        if matrizmaquinaZero():
            print("Você destruiu todos os barcos!\nFim de Jogo") 
            break
        
        ##jogada da maquina
        print(("Rodada da maquina..."))

        while True:

            ataquelinhaMaquina = random.randint(0,4)
            ataquecolunaMaquina = random.randint(0,9)

            if matrizmaquina2[ataquelinhaMaquina][ataquecolunaMaquina] == 0:
                matrizmaquina2[ataquelinhaMaquina][ataquecolunaMaquina] = 1
                break

        if matrizjogador[ataquelinhaMaquina][ataquecolunaMaquina] != 0:
            print("A maquina acertou!")
            matrizjogador[ataquelinhaMaquina][ataquecolunaMaquina] = 0

        else:
            print("A maquina errou")

        if matrizjogadorZero():
            print("A maquina destruiu todos os seus barcos =/\nFim de jogo")
            break

##outras funcoes

##essa função verifica se todos os barcos do jogador foram destruidos
def matrizjogadorZero():
    for linha in matrizjogador:
        for valor in linha:
            if valor != 0:
                return False

    return True
  
##essa função verifica se todos os barcos da maquina foram destruidos
def matrizmaquinaZero():
    for linha in matrizmaquina:
        for valor in linha:
            if valor != 0:
                return False

    return True

##essa funcao mostra a matriz do jogador
def mostrarMatrizJogador():
    for i in matrizjogador:
        print(i)

##essa funcao mostra a matriz da maquina
def mostrarMatrizMaquina():
    for i in matrizmaquina:
        print(i)


def main():
    while (True):
        mododeJogo = int(input("Qual modo de jogo deseja:\n0 - Clássico\n1 - Desafio\n"))

        if mododeJogo == 0:
            escolhaBarcoJogador()
            escolhaBarcoMaquina()
            jogo()

        elif mododeJogo == 1:
            escolhaFrotaJogador()
            escolhaFrotaMaquina()
            jogo()
        
        else:
            print("Opção inválida")
            
main()

