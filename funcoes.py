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

    for navios in info_navios:
        navio = info_navios[navios]
        for i in range(len(navio)):
            x = navio[i]
            for j in range(len(x)):
                y = x[j]
                tabuleiro[y[0]][y[1]] = 1
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

