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
    print(f"Escolha 5 posições para colocar seus barcos")
    while barcosJogador < 5:
        posicaolinha = int(input("Linha: "))
        if posicaolinha < 0 or posicaolinha > 4:
            print(f"Posição inválida")
            continue

        posicaocoluna = int(input("Coluna: "))
        if posicaocoluna < 0 or posicaocoluna > 9:
            print(f"Posição inválida")
            continue

        if matrizjogador[posicaolinha][posicaocoluna] == 1:
            print(f"Um barco ja está locado nessa posição")
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
def posicionarBarco(nome,valor):
    while True:

        escolhaHV = int(input(f"Escolha uma posicao para o seu {nome} ({valor} casas).\nHorizontal - 0\nVertical - 1\n"))
        livre = True

        if escolhaHV == 0:
            linha = int(input(f"Linha: "))
            coluna = int(input(f"Coluna: "))

            if linha < 0 or linha > 4:
                print(f"Posicao invalida.")
                continue

            if coluna + valor - 1 < 0 or coluna + valor - 1 > 9:
                print(f"Posicao invalida.")
                continue
            
            for i in range(valor):
                if matrizjogador[linha][coluna + i] != 0:
                    livre = False
                    break    

            if livre:
                for i in range(valor):
                    matrizjogador[linha][coluna + i] = valor

                mostrarMatrizJogador()
                print(f"{nome} posicionado!")
                break
                
            else:
                print(f"Ja existe uma frota nessa posicao.")
                continue
            
        elif escolhaHV == 1:
            linha = int(input(f"Linha: "))
            coluna = int(input(f"Coluna: "))

            if coluna < 0 or coluna > 9:
                print(f"Posicao invalida.")
                continue

            if linha + valor - 1 < 0 or linha + valor - 1 > 4:
                print(f"Posicao invalida.")
                continue
            
            for i in range(valor):
                if matrizjogador[linha + i][coluna] != 0:
                    livre = False
                    break    

            if livre:
                for i in range(valor):
                    matrizjogador[linha + i][coluna] = valor

                mostrarMatrizJogador()
                print(f"{nome} posicionado!")
                break

            else:
                print(f"Ja existe uma frota nessa posicao.")
                continue

        else:
            print(f"Valor invalido.")

##essa funcao define em quais posicoes a maquina colocou as 5 frotas                 
def posicionarBarcoMaquina(nome,valor):  
    while True:

        escolhaHV = random.randint(0,1)
        linha = random.randint(0,4)
        coluna = random.randint(0,9)
        livre = True

        if escolhaHV == 0:

            if coluna + valor - 1 > 9:
                continue

            for i in range(valor):
                if matrizmaquina[linha][coluna + i] != 0:
                    livre = False
                    break    

            if livre:
                for i in range(valor):
                    matrizmaquina[linha][coluna + i] = valor
                break
                
            else:
                continue
            
        elif escolhaHV == 1:
            if linha + valor - 1 > 4:
                continue

            for i in range(valor):
                if matrizmaquina[linha + i][coluna] != 0:
                    livre = False
                    break    

            if livre:
                for i in range(valor):
                    matrizmaquina[linha + i][coluna] = valor
                break

            else:
                continue

            

##essa funcao define os valores das frotas
def escolhaFrotaJogador():

    posicionarBarco(f"Porta-Aviões", 5)
    posicionarBarco(f"Navio-Tanque", 4)
    posicionarBarco(f"Contratorpedeiro", 3)
    posicionarBarco(f"Submarino", 2)
    posicionarBarco(f"Destroyer", 1)

def escolherTodasFrotasMaquina():

    posicionarBarcoMaquina(f"Porta-Aviões", 5)
    posicionarBarcoMaquina(f"Navio-Tanque", 4)
    posicionarBarcoMaquina(f"Contratorpedeiro", 3)
    posicionarBarcoMaquina(f"Submarino", 2)
    posicionarBarcoMaquina(f"Destroyer", 1)
    
##gameplay

##essa função é a gameplay do jogo
def jogo():
    while (True):

        ##jogada do jogador
        print(f"Escolha uma posição para atacar!")

        ataquelinhaJogador = int(input("Linha: "))
        if ataquelinhaJogador < 0 or ataquelinhaJogador > 4:
            print(f"Ataque inválido")
            continue

        ataquecolunaJogador = int(input("Coluna: "))
        if ataquecolunaJogador < 0 or ataquecolunaJogador > 9:
            print(f"Ataque inválido")
            continue

        if matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] == 'X' or matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] == 'N':
            print(f"Você já atacou essa posição!")
            continue

        if matrizmaquina[ataquelinhaJogador][ataquecolunaJogador] != 0:
            print(f"Acertou!")
            matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] = 'X'
            matrizmaquina[ataquelinhaJogador][ataquecolunaJogador] = 0

        else:
            print(f"Errou")
            matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] = 'N'

        for linha in matrizjogador2:
            print(linha)

        if matrizmaquinaZero():
            print(f"Você destruiu todos os barcos!\nFim de Jogo") 
            break
        
        ##jogada da maquina
        print((f"Rodada da maquina..."))

        while True:

            ataquelinhaMaquina = random.randint(0,4)
            ataquecolunaMaquina = random.randint(0,9)

            if matrizmaquina2[ataquelinhaMaquina][ataquecolunaMaquina] == 0:
                matrizmaquina2[ataquelinhaMaquina][ataquecolunaMaquina] = 1
                break

        if matrizjogador[ataquelinhaMaquina][ataquecolunaMaquina] != 0:
            print(f"A maquina acertou!")
            matrizjogador[ataquelinhaMaquina][ataquecolunaMaquina] = 0

        else:
            print(f"A maquina errou")

        if matrizjogadorZero():
            print(f"A maquina destruiu todos os seus barcos =/\nFim de jogo")
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
        mododeJogo = int(input(f"Qual modo de jogo deseja:\n0 - Clássico\n1 - Desafio\n"))

        if mododeJogo == 0:
            escolhaBarcoJogador()
            escolhaBarcoMaquina()
            jogo()

        elif mododeJogo == 1:
            escolhaFrotaJogador()
            escolherTodasFrotasMaquina()
            jogo()
        
        else:
            print(f"Opção inválida")
            
main()

