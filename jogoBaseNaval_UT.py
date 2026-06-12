import random

##matriz onde o jogador coloca suas frotas
matrizjogador = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

##matriz onde a maquina coloca suas frotas
matrizmaquina = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

##matriz para mostrar os ataques do jogador
matrizjogador2 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

##matriz para mostrar as posições que a maquina ataca, junto das frotas do jogador
matrizmaquina2 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

##matriz para registrar posições já atacadas pela máquina
matrizmaquina3 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

portaAvioesAfundado = False
navioTanqueAfundado = False
contratorpedeiroAfundado = False
submarinoAfundado = False
destroyerAfundado = False

portaAvioesAfundadoMaquina = False
navioTanqueAfundadoMaquina = False
contratorpedeiroAfundadoMaquina = False
submarinoAfundadoMaquina = False
destroyerAfundadoMaquina = False

##modo de jogo clássico

##essa função define em quais posições o jogador colocou os barcos
def escolhaBarcoJogador():
    barcosJogador = 0
    print(f"Escolha 5 posições para colocar seus barcos")
    while barcosJogador < 5:
        posicaolinha = lerInteiro("Linha: ")
        if posicaolinha < 0 or posicaolinha > 4:
            print(f"Posição inválida")
            continue

        posicaocoluna = lerInteiro("Coluna: ")
        if posicaocoluna < 0 or posicaocoluna > 9:
            print(f"Posição inválida")
            continue

        if matrizjogador[posicaolinha][posicaocoluna] == 1:
            print(f"Um barco ja está locado nessa posição")
            continue
             
        matrizjogador[posicaolinha][posicaocoluna] = 1
        matrizmaquina2[posicaolinha][posicaocoluna] = 1
        barcosJogador += 1
        mostrarTabuleiro(matrizjogador, f"SEU TABULEIRO")

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

        escolhaHV = lerInteiro(f"Escolha uma posição para o seu {nome} ({valor} casas).\nHorizontal - 0\nVertical - 1\n")
        livre = True

        if escolhaHV == 0:
            linha = lerInteiro("Linha: ")
            coluna = lerInteiro("Coluna: ")

            if linha < 0 or linha > 4:
                print(f"Posição inválida.")
                continue

            if coluna + valor - 1 < 0 or coluna + valor - 1 > 9:
                print(f"Posição inválida.")
                continue
            
            for i in range(valor):
                if matrizjogador[linha][coluna + i] != 0:
                    livre = False
                    break    

            if livre:
                for i in range(valor):
                    matrizjogador[linha][coluna + i] = valor
                    matrizmaquina2[linha][coluna + i] = valor

                mostrarTabuleiro(matrizjogador, f"SEU TABULEIRO")
                print(f"{nome} posicionado!")
                break
                
            else:
                print(f"Ja existe uma frota nessa posição.")
                continue
            
        elif escolhaHV == 1:
            linha = lerInteiro("Linha: ")
            coluna = lerInteiro("Coluna: ")

            if coluna < 0 or coluna > 9:
                print(f"Posicao inválida.")
                continue

            if linha + valor - 1 < 0 or linha + valor - 1 > 4:
                print(f"Posicao inválida.")
                continue
            
            for i in range(valor):
                if matrizjogador[linha + i][coluna] != 0:
                    livre = False
                    break    

            if livre:
                for i in range(valor):
                    matrizjogador[linha + i][coluna] = valor
                    matrizmaquina2[linha + i][coluna] = valor

                mostrarTabuleiro(matrizjogador, f"SEU TABULEIRO")
                print(f"{nome} posicionado!")
                break

            else:
                print(f"Ja existe uma frota nessa posição.")
                continue

        else:
            print(f"Valor inválido.")

##essa funcao define em quais posicoes a maquina colocou as 5 frotas                 
def posicionarBarcoMaquina(valor):  
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

    posicionarBarco(f"Porta Aviões", 5)
    posicionarBarco(f"Navio Tanque", 4)
    posicionarBarco(f"Contratorpedeiro", 3)
    posicionarBarco(f"Submarino", 2)
    posicionarBarco(f"Destroyer", 1)

def escolherTodasFrotasMaquina():

    posicionarBarcoMaquina(5)
    posicionarBarcoMaquina(4)
    posicionarBarcoMaquina(3)
    posicionarBarcoMaquina(2)
    posicionarBarcoMaquina(1)
    
##gameplay

##essa função é a gameplay do classico
def jogo():

    barcosRestantes = 5

    while (True):

        ##jogada do jogador
        print(f"Escolha uma posição para atacar!")

        ataquelinhaJogador = lerInteiro("Linha: ")
        if ataquelinhaJogador < 0 or ataquelinhaJogador > 4:
            print(f"Ataque inválido.")
            continue

        ataquecolunaJogador = lerInteiro("Coluna: ")
        if ataquecolunaJogador < 0 or ataquecolunaJogador > 9:
            print(f"Ataque inválido.")
            continue

        if matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] == 'X' or matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] == 'N':
            print(f"Você já atacou essa posição!")
            continue

        if matrizmaquina[ataquelinhaJogador][ataquecolunaJogador] != 0:
            matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] = 'X'
            matrizmaquina[ataquelinhaJogador][ataquecolunaJogador] = 0
            mostrarTabuleiro(matrizjogador2, f"SEU TABULEIRO")
            barcosRestantes -= 1
            print(f"Acertou!\nRestam: {barcosRestantes} barcos")
            

        else:
            matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] = 'N'
            mostrarTabuleiro(matrizjogador2, f"SEU TABULEIRO")
            print(f"Errou\nRestam: {barcosRestantes} barcos")

        if matrizmaquinaZero():
            print(f"Você destruiu todos os barcos!\nFim de Jogo.\nJogo feito por Mateus Yuri e Dhouglas Vinicius.") 
            break
        
        ##jogada da maquina
        print((f"Rodada da maquina..."))

        while True:

            ataquelinhaMaquina = random.randint(0,4)
            ataquecolunaMaquina = random.randint(0,9)

            if matrizmaquina3[ataquelinhaMaquina][ataquecolunaMaquina] == 0:
                matrizmaquina3[ataquelinhaMaquina][ataquecolunaMaquina] = 1
                break

        if matrizjogador[ataquelinhaMaquina][ataquecolunaMaquina] != 0:
            print(f"A maquina acertou!")
            matrizmaquina2[ataquelinhaMaquina][ataquecolunaMaquina] = 'X'
            matrizjogador[ataquelinhaMaquina][ataquecolunaMaquina] = 0

        else:
            matrizmaquina2[ataquelinhaMaquina][ataquecolunaMaquina] = 'N'
            print(f"A maquina errou")

        mostrarTabuleiro(matrizmaquina2, f"TABULEIRO DA MAQUINA")

        if matrizjogadorZero():
            print(f"A maquina destruiu todos os seus barcos =/\nFim de jogo.\nJogo feito por Mateus Yuri e Dhouglas Vinicius.")
            break

##essa função é a gameplay do desafio
def jogoDesafio():

    global portaAvioesAfundado
    global navioTanqueAfundado
    global contratorpedeiroAfundado
    global submarinoAfundado
    global destroyerAfundado

    global portaAvioesAfundadoMaquina
    global navioTanqueAfundadoMaquina
    global contratorpedeiroAfundadoMaquina
    global submarinoAfundadoMaquina
    global destroyerAfundadoMaquina

    while (True):

        ##jogada do jogador
        print(f"Escolha uma posição para atacar!")

        ataquelinhaJogador = lerInteiro("Linha: ")
        if ataquelinhaJogador < 0 or ataquelinhaJogador > 4:
            print(f"Ataque inválido.")
            continue

        ataquecolunaJogador = lerInteiro("Coluna: ")
        if ataquecolunaJogador < 0 or ataquecolunaJogador > 9:
            print(f"Ataque inválido.")
            continue

        if matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] == 'X' or matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] == 'N':
            print(f"Você já atacou essa posição!")
            continue

        if matrizmaquina[ataquelinhaJogador][ataquecolunaJogador] != 0:
            matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] = 'X'
            matrizmaquina[ataquelinhaJogador][ataquecolunaJogador] = 0
            mostrarTabuleiro(matrizjogador2, f"SEU TABULEIRO")
            print(f"Acertou!")

            if not portaAvioesAfundadoMaquina and barcoAbatidoMaquina(5):
                print("Você afundou um Porta Aviões!")
                portaAvioesAfundadoMaquina = True

            if not navioTanqueAfundadoMaquina and barcoAbatidoMaquina(4):
                print("Você afundou um Navio Tanque!")
                navioTanqueAfundadoMaquina = True

            if not contratorpedeiroAfundadoMaquina and barcoAbatidoMaquina(3):
                print("Você afundou um Contratorpedeiro!")
                contratorpedeiroAfundadoMaquina = True

            if not submarinoAfundadoMaquina and barcoAbatidoMaquina(2):
                print("Você afundou um Submarino!")
                submarinoAfundadoMaquina = True

            if not destroyerAfundadoMaquina and barcoAbatidoMaquina(1):
                print("Você afundou um Destroyer!")
                destroyerAfundadoMaquina = True

        else:
            matrizjogador2[ataquelinhaJogador][ataquecolunaJogador] = 'N'
            mostrarTabuleiro(matrizjogador2, f"SEU TABULEIRO")
            print(f"Errou")

        if matrizmaquinaZero():
            print(f"Você destruiu todos os barcos!\nFim de Jogo.\nJogo feito por Mateus Yuri e Dhouglas Vinicius.") 
            break
        
        ##jogada da maquina
        print((f"Rodada da maquina..."))

        while True:

            ataquelinhaMaquina = random.randint(0,4)
            ataquecolunaMaquina = random.randint(0,9)

            if matrizmaquina3[ataquelinhaMaquina][ataquecolunaMaquina] == 0:
                matrizmaquina3[ataquelinhaMaquina][ataquecolunaMaquina] = 1
                break

        if matrizjogador[ataquelinhaMaquina][ataquecolunaMaquina] != 0:
            print(f"A maquina acertou!")
            matrizmaquina2[ataquelinhaMaquina][ataquecolunaMaquina] = 'X'
            matrizjogador[ataquelinhaMaquina][ataquecolunaMaquina] = 0

            if not portaAvioesAfundado and barcoAbatido(5):
                print("A maquina afundou seu Porta Aviões!")
                portaAvioesAfundado = True

            if not navioTanqueAfundado and barcoAbatido(4):
                print("A maquina afundou seu Navio Tanque!")
                navioTanqueAfundado = True

            if not contratorpedeiroAfundado and barcoAbatido(3):
                print("A maquina afundou seu Contratorpedeiro!")
                contratorpedeiroAfundado = True

            if not submarinoAfundado and barcoAbatido(2):
                print("A maquina afundou seu Submarino!")
                submarinoAfundado = True

            if not destroyerAfundado and barcoAbatido(1):
                print("A maquina afundou seu Destroyer!")
                destroyerAfundado = True

        else:
            matrizmaquina2[ataquelinhaMaquina][ataquecolunaMaquina] = 'N'
            print(f"A maquina errou")

        mostrarTabuleiro(matrizmaquina2, f"TABULEIRO DA MAQUINA")

        if matrizjogadorZero():
            print(f"A maquina destruiu todos os seus barcos =/\nFim de jogo.\nJogo feito por Mateus Yuri e Dhouglas Vinicius.")
            break

        

##outras funcoes

##essa função analisa se o barco do jogador foi afundado
def barcoAbatido(valorBarco):
    for linha in matrizjogador:
        if valorBarco in linha:
            return False
    return True

# [CORREÇÃO] Nova função que analisa se o barco da máquina foi afundado
def barcoAbatidoMaquina(valorBarco):
    for linha in matrizmaquina:
        if valorBarco in linha:
            return False
    return True

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

##essa função evita crash ao digitar texto onde se espera número
def lerInteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print(f"Valor inválido.")

##essa funcao mostra a matriz como tabuleiro
def mostrarTabuleiro(matriz, titulo):
    print(f"\n{'=' * 10} {titulo} {'=' * 10}")

    print("    ", end="")
    for i in range(10):
        print(f"{i:^3}", end="")
    print()

    print("   +" + "---" * 10)

    for linha in range(5):
        print(f"{linha:2} |", end="")
        for coluna in range(10):
            print(f"{str(matriz[linha][coluna]):^3}", end="")
        print()

##essa função mostra o tutorial
def tutorial():
    print("""
╔══════════════════════════════════════════════════════════╗
║                    BATALHA NAVAL                         ║
╠══════════════════════════════════════════════════════════╣
║ OBJETIVO                                                 ║
║ Destruir toda a frota inimiga antes que a máquina        ║
║ destrua a sua.                                           ║
╠══════════════════════════════════════════════════════════╣
║ TABULEIRO                                                ║
║ O jogo utiliza um tabuleiro de 5 linhas por 10 colunas.  ║
║                                                          ║
║ Linhas:  0 até 4                                         ║
║ Colunas: 0 até 9                                         ║
║                                                          ║
║ EXEMPLO:                                                 ║
║ Linha: 2                                                 ║
║ Coluna: 7                                                ║
╠══════════════════════════════════════════════════════════╣
║ MODO CLÁSSICO                                            ║
║ • Cada jogador possui 5 embarcações.                     ║
║ • Cada embarcação ocupa apenas 1 posição.                ║
║ • Um acerto afunda imediatamente a embarcação.           ║
║ • Vence quem destruir todas as embarcações inimigas.     ║
╠══════════════════════════════════════════════════════════╣
║ MODO DESAFIO                                             ║
║                                                          ║
║ FROTAS DISPONÍVEIS:                                      ║
║                                                          ║
║ Porta-Aviões      -> 5 posições                          ║
║ Navio-Tanque      -> 4 posições                          ║
║ Contratorpedeiro  -> 3 posições                          ║
║ Submarino         -> 2 posições                          ║
║ Destroyer         -> 1 posição                           ║
║                                                          ║
║ REGRAS:                                                  ║
║ • As embarcações podem ser posicionadas na horizontal    ║
║   ou vertical.                                           ║
║ • Não é permitido sobrepor embarcações.                  ║
║ • Uma embarcação só afunda quando TODAS as suas          ║
║   posições forem destruídas.                             ║
║ • O jogador que destruir toda a frota inimiga vence.     ║
╠══════════════════════════════════════════════════════════╣
║ LEGENDA                                                  ║
║                                                          ║
║ 0 = Posição não atacada                                  ║
║ X = Acerto                                               ║
║ N = Erro                                                 ║
╠══════════════════════════════════════════════════════════╣
║ COMO JOGAR                                               ║
║                                                          ║
║ 1. Escolha um modo de jogo.                              ║
║ 2. Posicione suas embarcações.                           ║
║ 3. Escolha uma linha (0 a 4).                            ║
║ 4. Escolha uma coluna (0 a 9).                           ║
║ 5. Aguarde o resultado do ataque.                        ║
║ 6. Continue jogando até destruir toda a frota inimiga.   ║
╠══════════════════════════════════════════════════════════╣
║                 Boa sorte, comandante!                   ║
╚══════════════════════════════════════════════════════════╝
""")


def main():
    while (True):
        mododeJogo = lerInteiro("Qual modo de jogo deseja:\n0 - Clássico\n1 - Desafio\n2 - Tutorial\n")

        if mododeJogo == 0:
            escolhaBarcoJogador()
            escolhaBarcoMaquina()
            jogo()
            break

        elif mododeJogo == 1:
            escolhaFrotaJogador()
            escolherTodasFrotasMaquina()
            jogoDesafio()
            break

        elif mododeJogo == 2:
            tutorial()
            
        
        else:
            print(f"Opção inválida")
            
main()
