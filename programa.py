import random

def define_posicoes(linha,coluna,orientacao,tamanho):
    x = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            x.append([linha+i,coluna])
        elif orientacao == 'horizontal':
            x.append([linha,coluna+i])
    return x

def preenche_frota(frota,nome_do_navio,linha,coluna,orientacao,tamanho):
    posicao = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome_do_navio not in frota:
        frota[nome_do_navio] = [posicao]
    else:
        frota[nome_do_navio].append(posicao)
    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota(info_navios):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0]*10)

    for nome in info_navios:
        navios = info_navios[nome]
        for navio in navios:
            for posicao in navio:
                tabuleiro[posicao[0]][posicao[1]] = 1
    return tabuleiro

def afundados(frota, tabuleiro):
    cont = 0
    for nome in frota:
        navios = frota[nome]
        for navio in navios:
            afundado = True
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    afundado = False
            if afundado:
                cont += 1
    return cont

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in novas:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
        for nome in frota:
            for navio in frota[nome]:
                if posicao in navio:
                    return False
    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

frota = {}
nomes = ["porta-aviões", "navio-tanque", "contratorpedeiro", "submarino"]
quantidades = [1, 2, 3, 4]
tamanhos = [4, 3, 2, 1]

for i in range(len(nomes)):
    nome = nomes[i]
    tamanho = tamanhos[i]
    for k in range(quantidades[i]):
        valido = False
        while not valido:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if tamanho == 1:
                orientacao = "horizontal"
            else:
                escolha = int(input("Orientação: [1] Vertical [2] Horizontal "))
                if escolha == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valido = True
            else:
                print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios = 0
for nome in frota_oponente:
    total_navios += len(frota_oponente[nome])

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    repetida = True
    while repetida:
        linha = int(input("Jogador, qual linha deseja atacar? "))
        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if tabuleiro_oponente[linha][coluna] == 'X' or tabuleiro_oponente[linha][coluna] == '-':
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        else:
            repetida = False

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False


    else:
        sorteando = True
        while sorteando:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if tabuleiro_jogador[linha][coluna] != 'X' and tabuleiro_jogador[linha][coluna] != '-':
                sorteando = False

        print(f"Seu oponente está atacando na linha {linha} e coluna {coluna}")
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha, coluna)

        if afundados(frota, tabuleiro_jogador) == total_navios:
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False
