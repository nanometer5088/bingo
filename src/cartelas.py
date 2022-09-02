from constants import LOGGING, ERRORS, SELECTED
from funcoes import learquivo, escrevearquivo, cleanup
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
    from funcoes import aleatorio
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
def maketable(elemento_inicial, lista, playerselect, backend_results):
    from funcoes import aleatorio
    from prettytable import PrettyTable, DOUBLE_BORDER
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

    elif elemento_inicial == "":
        random = aleatorio(1, 50)
        print(f"""
***************************************************
**         Número Sorteado: {random}                    **
***************************************************
    """) if random < 10 else print(f"""
***************************************************
**         Número Sorteado: {random}                   **
***************************************************
    """)

        for i in range(4):
            if random in lista[i]:
                elemento = (lista[i].index(random))
                lista[i][elemento] = f'[{lista[i][elemento]}]'


    elif elemento_inicial != "1" or elemento_inicial != "2" or elemento_inicial != "3" or elemento_inicial != "4" or elemento_inicial != "":
        playerselect[0] = SELECTED["notplayer"]
        playerselect[1] = SELECTED["notplayer"]
        playerselect[2] = SELECTED["notplayer"]
        playerselect[3] = SELECTED["notplayer"]
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
    x.set_style(DOUBLE_BORDER)
    #
    return x

def TUI_principal():
    import os
    elemento_inicial = "1"
    playerselect = [0] * 4
    backend_results = [0] * 4
    for i in range(len(backend_results)):
        playerselect[i] = [0] * 5
    lista = cartelas_show()
    while True:
        os.system("cls || clear")
        elemento_inicial = input(maketable(elemento_inicial, lista, playerselect, backend_results))
TUI_principal()