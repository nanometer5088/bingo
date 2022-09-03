from src.constants import ERRORS, SELECTED, SCOREBOARD
from src.funcoes import learquivo, escrevearquivo, cleanup, aleatorio
def listas():
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
    cartelas = listas()
    resultado = [0] * 4
    randomold = 0
    #Diminuindo as chances de vir 2 resultados idênticos
    for i in range(4):
        random = aleatorio(0, (len(cartelas) - 1)) 
        if random == randomold:
            random = aleatorio(0, (len(cartelas) - 1))

        cartelatemp = cartelas[random]
        resultado[i] = cartelatemp
        random = randomold
    return resultado

def donotabela(elemento_inicial):
            print(f"""
***************************************************
**         Você agora é dono da cartela {elemento_inicial}        **
***************************************************
    """)

def numerosorteado(random):
    print(f"""
***************************************************
**         Número Sorteado: {random}                    **
***************************************************
    """) if random < 10 else print(f"""
***************************************************
**         Número Sorteado: {random}                   **
***************************************************
    """)
def maketable(elemento_inicial, lista, playerselect, backend_results, modelovitoria, resultado):
    from src.funcoes import aleatorio
    from prettytable import PrettyTable, DOUBLE_BORDER, DEFAULT

    #Alterar a posição do jogador na tabela
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

    #Sorteio
    elif elemento_inicial == "":
        random = aleatorio(1, 50)
        numerosorteado(random)

        for i in range(4):
            if random in lista[i]:
                elemento = (lista[i].index(random))
                lista[i][elemento] = f'-{lista[i][elemento]}-'
                backend_results[i][elemento] = 1
        for i in range(4):
            if backend_results[i] == modelovitoria:
                for a in range(4):
                    if playerselect[a] == SELECTED["player"]:
                        if i == a:
                            resultado = "vitoria"
                        else:
                            resultado = "derrota"

    #Erro - item inválido
    elif elemento_inicial != "1" or elemento_inicial != "2" or elemento_inicial != "3" or elemento_inicial != "4" or elemento_inicial != "":
        print(f"""
    {ERRORS["invalid"]}
    Valores possíveis: 1, 2, 3, 4, 5
    """)
    #Prettytable code
    x = PrettyTable()
    x.field_names = ["Dono", "1", "2", "3", "4", "5"]
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
    #
    return resultado

def TUI_principal():
    import os, datetime
    resultado = ""
    modelovitoria = [1, 1, 1, 1, 1]
    elemento_inicial = "1"
    principal = ""
    playerselect = [0] * 4
    backend_results = [0] * 4
    for i in range(len(backend_results)):
        backend_results[i] = [0] * 5
    lista = cartelas_show()

    while principal == "":
        os.system("cls || clear")
        principal = maketable(elemento_inicial, lista, playerselect, backend_results, modelovitoria, resultado)
        elemento_inicial = input()
    if principal == "vitoria":
        nome = input(SCOREBOARD["win"])
        arquivo = open('vencedores.txt', 'a')
        arquivo.write(f'{datetime.datetime.now()} - {nome}\n')
        arquivo.close()
    if principal == "derrota":
        print(SCOREBOARD["loss"])