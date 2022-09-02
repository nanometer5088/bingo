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

def maketable(elemento_inicial, lista):
    from funcoes import aleatorio, learquivo, escrevearquivo, cleanup
    from constants import SELECTED, ERRORS
    from prettytable import PrettyTable, DOUBLE_BORDER
    playerselect = [0] * 4
    if elemento_inicial == "1":
        playerselect[0] = SELECTED["player"]
        playerselect[1] = SELECTED["notplayer"]
        playerselect[2] = SELECTED["notplayer"]
        playerselect[3] = SELECTED["notplayer"]
    elif elemento_inicial == "2":
        playerselect[0] = SELECTED["notplayer"]
        playerselect[1] = SELECTED["player"]
        playerselect[2] = SELECTED["notplayer"]
        playerselect[3] = SELECTED["notplayer"]
    elif elemento_inicial == "3":
        playerselect[0] = SELECTED["notplayer"]
        playerselect[1] = SELECTED["notplayer"]
        playerselect[2] = SELECTED["player"]
        playerselect[3] = SELECTED["notplayer"]
    elif elemento_inicial == "4":
        playerselect[0] = SELECTED["notplayer"]
        playerselect[1] = SELECTED["notplayer"]
        playerselect[2] = SELECTED["notplayer"]
        playerselect[3] = SELECTED["player"]

    elif elemento_inicial == "":
        random = aleatorio(1, 50)
        randomparaarquivo = random - 1
        print(f"""
***************************************************
**         Número Sorteado: {random}                    **
***************************************************
    """
    )

        for i in range(4):
            if random in lista[i]:
                elemento = (lista[i].index(random))
                lista[i][elemento] = f'*{lista[i][elemento]}*'


    elif elemento_inicial != "1" or elemento_inicial != "2" or elemento_inicial != "3" or elemento_inicial != "4" or elemento_inicial != "":
        playerselect[0] = SELECTED["notplayer"]
        playerselect[1] = SELECTED["notplayer"]
        playerselect[2] = SELECTED["notplayer"]
        playerselect[3] = SELECTED["notplayer"]
        print(f"""
    {ERRORS["invalid"]}
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
    print(lista)
    return x

def TUI_principal():
    import os
    elemento_inicial = "1"
    lista = cartelas_show()
    while True:
        os.system("cls || clear")
        elemento_inicial = input(maketable(elemento_inicial, lista))
TUI_principal()
