numero_de_linhas = 20  # DEFINIMOS A MATRIZ PRINCIPAL COM 20 LINHAS
numero_de_colunas = 20  # DEFINIMOS A MATRIZ PRINCIPAL COM 20 COLUNAS
contador_de_acertos_porta_aviao = 0  # DECLARAÇÃO DE VARIAVÉL PARA QUANDO O JOGADOR 2 ACERTAR UM PORTA AVIÃO
contador_de_acertos_fragata = 0  # DECLARAÇÃO DE VARIAVÉL PARA QUANDO O JOGADOR 2 ACERTAR UMA FRAGATA
contador_de_acertos_cruzador = 0  # DECLARAÇÃO DE VARIAVÉL PARA QUANDO O JOGADOR 2 ACERTAR UM CRUZADOR
coluna_horizontal = '    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20'  # DECLARAÇÃO DE UMA STRING PARA RECEBER AS COLUNAS.
linha_vertical = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T']  # DECLARAÇÃO DE UMA LISTA PARA RECEBER AS LINHAS
posicoes_atacadas = []  # CRIAÇÃO DE UMA LUSTA PARA RECEBER AS POSIÇÕES ATACADAS
posicoes_acertadas = []  # CRIAÇÃO DE UMA LUSTA PARA RECEBER AS POSIÇÕES ACERTADAS
pontuacao_total = 0

def criar_matriz():  # CRIAÇÃO DE UMA FUNÇÃO PARA CRIAR UMA MATRIZ
    matriz = ["#"] * numero_de_linhas
    for linha in range(numero_de_linhas):
        matriz[linha] = ["#"] * numero_de_colunas
    return matriz


def imprimir_matriz(matriz):  # CRIAÇÃO DE UMA FUNÇÃO PARA IMPRIMIR UMA MATRIZ
    linha_matriz = ' '
    print(coluna_horizontal)

    for linha in range(numero_de_linhas):
        linha_matriz += linha_vertical[linha] + '  '
        for coluna in range(numero_de_colunas):
            linha_matriz += matriz[linha][coluna] + "  "
        linha_matriz += linha_vertical[linha] + ' '
        print(linha_matriz)
        linha_matriz = ' '
    print(coluna_horizontal)


def imprimir_informativo():  # CRIAÇÃO DE UMA FUNÇÃO PARA IMPRIMIR  UM iINFORMATIVO AO USUÁRIO
    print("--------------------------------------------------")
    print("ESCOLHA EM QUAL POSIÇÃO,VOCÊ QUER ESCONDER ESSE VEICULO MILITAR:")
    print("----------------------------")
    print("DISPONIBILIDADE DE VEÍCULOS MILITARES:")
    print("3xPORTA AVIÃO")
    print("4XCRUZADOR")
    print("5xFRAGATA")
    print("----------------------------")
    print("OS VEÍCULOS SÃO DEFINIDOS:")
    print("PORTA-AVIÃO=1")
    print("CRUZADOR=2")
    print("FRAGTA=3")


imprimir_informativo()


def procurando_linha(letra):  # CRIAÇÃO DE UMA FUNÇÃO PARA AS LETRAS SEREM CONVERTIDAS EM LINHAS
    for index_linha in range(numero_de_linhas):
        if linha_vertical[index_linha] == letra:
            return index_linha
    return -1



def buscando_as_coordenadas():  # CRIAÇÃO DE UMA FUNÇÃO PARA BUSCAR AS POSIÇOES PARA ESCONDER AS EMBARCAÇÕES.
    linha = input("DIGITE UMA LINHA :")
    linha = procurando_linha(linha)
    while linha == -1:
        linha = input("DIGITE NOVAMENTE UMA LINHA VÁLIDA:")
        linha = procurando_linha(linha)
    coluna = int(input("DIGITE UMA COLUNA :")) - 1

    while coluna < 0 or coluna > 18:
        coluna = int(input("DIGITE NOVAMENTE UMA NOVA COLUNA :")) - 1

    return [linha, coluna]


def validando_as_posicoes(matriz, embarcacao,linha,coluna):  # CRIAÇÃO DE UMA FUNÇÃO PARA VALIDAR  AS COORDENADAS INSERIDAS PELO JOGADOR  1 PARA ESCONDER AS EMBARCAÇÕES.
    if embarcacao == "Porta-aviao":
        if coluna + 3 > 19:
            return False
        elif (matriz[linha][coluna] != '#' or matriz[linha][coluna + 1] != '#' or matriz[linha][
            coluna + 2] != '#' or matriz[linha][coluna + 3] != '#'):
            return False

    elif embarcacao == "Cruzador":
        if coluna + 2 > 19:
            return False
        elif matriz[linha][coluna] != "#" or matriz[linha][coluna + 1] != "#" or matriz[linha][coluna + 2] != "#":
            return False

    elif embarcacao == "Fragata":
        if coluna + 1 > 19:
            return False
        elif matriz[linha][coluna] != "#" or matriz[linha][coluna + 1] != "#":
            return False

    return True


def inserindo_as_embarcacoes_de_defesa(matriz):  # CRIAÇÃO DE UMA FUNÇÃO PARA O JOGADOR INSERE AS EMBARCACOES NA MATRIZ DE DEFESA.

    for embarcacao in range(12):
        if embarcacao < 3:
            print("INSERINDO OS PORTAS-AVIÕES")
            linha, coluna = buscando_as_coordenadas()
            while not validando_as_posicoes(matriz, "Porta-aviao", linha, coluna):
                print("FORMATO INVÁLIDO.")
                linha, coluna = buscando_as_coordenadas()
            matriz[linha][coluna] = "1"
            matriz[linha][coluna + 1] = "1"
            matriz[linha][coluna + 2] = "1"
            matriz[linha][coluna + 3] = "1"
            imprimir_matriz(matriz)
            print("------------------------------------------------------------------")
        elif embarcacao < 7:
            print("INSERINDO OS CRUZADORES:")
            linha, coluna = buscando_as_coordenadas()
            while not validando_as_posicoes(matriz, "Cruzador", linha, coluna):
                print("FORMATO INVÁLIDO.")
                linha, coluna = buscando_as_coordenadas()
            matriz[linha][coluna] = "2"
            matriz[linha][coluna + 1] = "2"
            matriz[linha][coluna + 2] = "2"
            imprimir_matriz(matriz)
            print("------------------------------------------------------------------")
        else:
            print("INSERINDO AS FRAGATAS:")
            linha, coluna = buscando_as_coordenadas()
            while not validando_as_posicoes(matriz, "Fragata", linha, coluna):
                print("FORMATO INVÁLIDO.")
                linha, coluna = buscando_as_coordenadas()
            matriz[linha][coluna] = "3"
            matriz[linha][coluna + 1] = "3"
            print("------------------------------------------------------------------")
            imprimir_matriz(matriz)
            print("------------------------------------------------------------------")
        imprimir_matriz(matriz)


def validando_ataque(linha,coluna):  # CRIACAO DE UMA FUNCAO PARA VALIDAR AS POSICOES DO JOGADOR 2 INSERIU PASA ATACAR OS NÁVIOS
    for posicao in posicoes_atacadas:
        if posicao[0] == linha and posicao[1] == coluna:
            return False
    return True



def pontuacao(embarcacao): # CRIACAO DE UMA FUNCAO PARA MOSTRAR A PONTIUACAO DO JOGADOR 2.
    global contador_de_acertos_porta_aviao, contador_de_acertos_fragata, contador_de_acertos_cruzador,pontuacao_total
    if embarcacao == '1':
        contador_de_acertos_porta_aviao += 1
        while contador_de_acertos_porta_aviao % 4 >= 1:
            print("VOCÊ ACERTOU A",contador_de_acertos_porta_aviao,"PARTE DO PORTA-AVIÃO.")
            break
        if contador_de_acertos_porta_aviao % 4 == 0:
            print("VOCÊ NAUFRAGOU UM PORTA-AVIÃO.")
            pontuacao_total += 30

    elif embarcacao == '2':
        contador_de_acertos_fragata += 1
        while contador_de_acertos_fragata % 3 >= 1:
            print("VOCÊ ACERTOU",contador_de_acertos_fragata,"PARTE DO CRUZADOR.")
            break
        if contador_de_acertos_fragata % 3 == 0:
            print("VOCÊ NAUFRAGOU UM CRUZADOR.")
            pontuacao_total += 20

    else:
        contador_de_acertos_cruzador += 1
        while contador_de_acertos_cruzador % 2 >= 1:
            print("VOCÊ ACERTOU",contador_de_acertos_cruzador,"PARTE DA FRAGATA.")
            break
        if contador_de_acertos_cruzador % 2 == 0:
            print("VOCÊ NAUFRAGOU UMA FRAGATA.")
            pontuacao_total += 10

# CRIANDO,IMPRIMINDO O MAPA DE DEFESA E INSERINDO OS NÁVIOS NAS POSICOES ORDENADAS NA MATRIZ DE DEFESA PELO JOGADOR 1
def atacando_os_navios(matriz_de_defesa,matriz_de_ataque):  # CRIACAO DE UMA FUNCAO PARA O JOGADOR 2 TENTAR AFUNDAR OS NÁVIOS ESCVNCODIDOS PELO JOGADOR 1.
    linha, coluna = buscando_as_coordenadas()
    while not validando_ataque(linha, coluna):
        print("VOCÊ JÁ ATACOU ESTA POSIÇÃO")
        linha, coluna = buscando_as_coordenadas()

    posicoes_atacadas.append([linha,coluna])

    if matriz_de_defesa[linha][coluna] != "#":
        matriz_de_ataque[linha][coluna] = "O"
        posicoes_acertadas.append([linha,coluna])
        pontuacao(matriz_de_defesa[linha][coluna])
    else:
        matriz_de_ataque[linha][coluna] = "X"
    posicoes_atacadas.append([linha,coluna])


tabuleiro_defesa = criar_matriz()
imprimir_matriz(tabuleiro_defesa)

inserindo_as_embarcacoes_de_defesa(tabuleiro_defesa)
tabuleiro_ataque = criar_matriz()
def parte_final():
    for cont in range(500):
        print()
    print('\n HORA DO ATAQUE\n')
    for cont in range(400):
        atacando_os_navios(tabuleiro_defesa, tabuleiro_ataque)
        imprimir_matriz(tabuleiro_ataque)
        global pontuacao_total
        print('\n SUA PONTUAÇÃO:', pontuacao_total)
        if len(posicoes_acertadas) == 34:
            print('\n VOCÊ NAUFRAGOU TODAS POSIÇÕES!!!\n')

            print('\n ✨PARABÉNS ,VOCÊ GANHOU✨ \n')
parte_final()
