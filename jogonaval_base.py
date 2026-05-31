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

        if matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] != 0:
            print("Você já atacou essa posição!")
            continue

        if matrizmaquina[ataquelinhaJogador][ataquecolunaJogador] == 1:
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

        if matrizjogador[ataquelinhaMaquina][ataquecolunaMaquina] == 1:
            print("A maquina acertou!")
            matrizjogador[ataquelinhaMaquina][ataquecolunaMaquina] = 0

        else:
            print("A maquina errou")

        if matrizjogadorZero():
            print("A maquina destruiu todos os seus barcos =/\nFim de jogo")
            break


##essa função verifica se todos os barcos do jogador foram destruidos
def matrizjogadorZero():
    for linha in matrizjogador:
        if 1 in linha:
            return False     
        
    return True
  
##essa função verifica se todos os barcos da maquina foram destruidos
def matrizmaquinaZero():
    for linha in matrizmaquina:
        if 1 in linha:
            return False
         
    return True
    

def main():
    escolhaBarcoJogador()
    escolhaBarcoMaquina()
    jogo()
    
main()

