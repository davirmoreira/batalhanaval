def define_posicoes(linha,coluna,orientacao,tamanho):
    x = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            x.append([linha+i,coluna])
        elif orientacao == 'horizontal':
            x.append([linha,coluna+i])
    return x
