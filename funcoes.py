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
