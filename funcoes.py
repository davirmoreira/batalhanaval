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
