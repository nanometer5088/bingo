from src.constants import ERRORS, SELECTED, SCOREBOARD, GAME
from src.funcoes import aleatorio
def listas():
#Geração de listas a partir do arquivo de cartelas. Essas listas são separadas em
#listas menores, que são separadas a partir da vírgula.
    i = 0
    vazio = ''
    arquivo = open('cartelas.txt', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    tamanho = len(linhas)
    arquivo.close()
    vet = [0] * tamanho
    arquivo = open('cartelas.txt', 'r', encoding='utf-8')
    while True:
        lelinha = arquivo.readline().rstrip()
        if lelinha == vazio:
            break
        vet[i] = lelinha.split(',')
        for a in range(5):
            vet[i][a] = int(vet[i][a])
        i += 1
    arquivo.close()
    return vet

def cartelas_show():
#Sorteia 4 cartelas dentre as 20 disponíveis
    cartelas = listas()
    resultado = [0] * 4
    randomold = 0
    #Elimina as chances de vir duas cartelas idênticas em sequência
    for i in range(4):
        random = aleatorio(0, (len(cartelas) - 1)) 
        if random == randomold:
            random = aleatorio(0, (len(cartelas) - 1))

        cartelatemp = cartelas[random]
        resultado[i] = cartelatemp
        random = randomold
    return resultado

def donotabela(elemento_inicial):
#Apresenta na tela uma indicação de qual cartela o usuário alternou
#Esse indicador é baseado no mostrado nas figuras da questão
    from colr import color
    print(f"""
***************************************************
**         Você agora é dono da cartela {color(elemento_inicial, fore=(76, 151, 237))}        **
***************************************************
    """)

def numerosorteado(random):
#Apresenta na tela uma indicação de qual número foi sorteado, e
#se alinha de acordo com o número de casas do número sorteado
#Esse indicador é baseado no mostrado nas figuras da questão
    from colr import color
    print(f"""
***************************************************
**         Número Sorteado: {color(random, fore=(76, 151, 237))}                    **
***************************************************
    """) if random < 10 else print(f"""
***************************************************
**         Número Sorteado: {color(random, fore=(76, 151, 237))}                   **
***************************************************
    """)
def maketable(elemento_inicial, lista, playerselect, backend_results, modelovitoria, resultado, random):
    from src.funcoes import aleatorio
    from prettytable import PrettyTable, DOUBLE_BORDER, DEFAULT
    from colr import color

    #Alterar a cartela escolhida pelo jogador na tabela
    #A cartela do jogador é indicada pelo símbolo "■"
    if elemento_inicial == "1":
        donotabela(elemento_inicial)
        playerselect[0], playerselect[1] = SELECTED["player"], SELECTED["notplayer"]
        playerselect[2], playerselect[3] = SELECTED["notplayer"], SELECTED["notplayer"]
    elif elemento_inicial == "2":
        donotabela(elemento_inicial)
        playerselect[0], playerselect[1] = SELECTED["notplayer"], SELECTED["player"]
        playerselect[2], playerselect[3] = SELECTED["notplayer"], SELECTED["notplayer"]
    elif elemento_inicial == "3":
        donotabela(elemento_inicial)
        playerselect[0], playerselect[1] = SELECTED["notplayer"], SELECTED["notplayer"]
        playerselect[2], playerselect[3] = SELECTED["player"], SELECTED["notplayer"]
    elif elemento_inicial == "4":
        donotabela(elemento_inicial)
        playerselect[0], playerselect[1] = SELECTED["notplayer"], SELECTED["notplayer"]
        playerselect[2], playerselect[3] = SELECTED["notplayer"], SELECTED["player"]

    #Sorteio dos números
    elif elemento_inicial == "":
        numerosorteado(random)

        #lógica de vitórias / derrotas
        for i in range(4):
            if random in lista[i]:
                elemento = (lista[i].index(random))
                lista[i][elemento] = color(f'{lista[i][elemento]}', fore=(238, 77, 77))
                backend_results[i][elemento] = 1
        for i in range(4):
            if backend_results[i] == modelovitoria:
                for a in range(4):
                    if playerselect[a] == SELECTED["player"]:
                        if i == a:
                            resultado = "vitoria"
                        else:
                            resultado = "derrota"

    #Determina se a entrada do usuário é inválida, e aje de acordo
    elif elemento_inicial != "1" or elemento_inicial != "2" or elemento_inicial != "3" or elemento_inicial != "4" or elemento_inicial != "":
        print(f"""
    {ERRORS["invalid"]}
    Valores possíveis: [1, 2, 3, 4]
    """)

    #Montagem e apresentação da tabela usando PrettyTable
    x = PrettyTable()
    x.field_names = ["Dono", "B", "I", "N", "G", "O"]
    x.add_rows(
        [
            [playerselect[0], lista[0][0], lista[0][1], lista[0][2], lista[0][3], lista[0][4]],
            [playerselect[1], lista[1][0], lista[1][1], lista[1][2], lista[1][3], lista[1][4]],
            [playerselect[2], lista[2][0], lista[2][1], lista[2][2], lista[2][3], lista[2][4]],
            [playerselect[3], lista[3][0], lista[3][1], lista[3][2], lista[3][3], lista[3][4]],
        ]
    )
    if resultado == "":
        x.set_style(DOUBLE_BORDER)
    else:
        x.set_style(DEFAULT)
    print(x)
    
    #Indica ao jogador as opções de escolha disponíveis
    print(GAME["presskey"])
    return resultado

def TUI_principal():
    import os, datetime
    from src.funcoes import geralistaaleatoria
    
    #Determina alguns valores importantes para o funcionamento do programa
    resultado = ""
    modelovitoria = [1, 1, 1, 1, 1]
    elemento_inicial = "1"
    principal = ""
    playerselect = [0] * 4
    backend_results = [0] * 4
    for i in range(len(backend_results)):
        backend_results[i] = [0] * 5

    #Busca as 4 cartelas aleatórias de cartelas_show() 
    lista = cartelas_show()

    #Busca a lista de números à serem sorteados
    listaaleatoria = geralistaaleatoria(50, 50)

    #Loop que roda maketable() até que haja algum status (Vitória ou derrota)
    i = -1
    while principal == "":
        os.system("cls || clear")
        random = listaaleatoria[i]
        principal = maketable(elemento_inicial, lista, playerselect, backend_results, modelovitoria, resultado, random)
        elemento_inicial = input()
        if elemento_inicial == "": 
            i += 1
    #Vitória
    #Abre/Cria um arquivo de vencedores, parabeniza o jogador e insere o nome
    #do jogador e a data/hora da partida no arquivo. Conteúdos prévios do arquivo
    #são mantidos, caso hajam vencedores anteriores
    if principal == "vitoria":
        nome = input(SCOREBOARD["win"])
        arquivo = open('vencedores.txt', 'a')
        arquivo.write(f'{datetime.datetime.now()} - {nome}\n')
        arquivo.close()

    #Derrota
    #Deseja ao jogador melhor sorte na próxima partida
    if principal == "derrota":
        print(SCOREBOARD["loss"])