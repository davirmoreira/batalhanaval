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
                escolha = int(input("[1] Vertical [2] Horizontal >"))
                if escolha == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valido = True
            else:
                print("Esta posição não está válida!")

print(frota)

          