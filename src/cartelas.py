def aleatorio(x, y):
    import random
    return random.randint(x, y)

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

def TUI_principal(elemento_inicial):
    from constants import SELECTED, ERRORS
    from prettytable import PrettyTable, DOUBLE_BORDER
    import os

    playerselect = [0] * 4
    lista = cartelas_show()
    while True:
        if int(elemento_inicial) == 1:
            playerselect[0] = SELECTED["player"]
            playerselect[1] = SELECTED["notplayer"]
            playerselect[2] = SELECTED["notplayer"]
            playerselect[3] = SELECTED["notplayer"]
        if int(elemento_inicial) == 2:
            playerselect[0] = SELECTED["notplayer"]
            playerselect[1] = SELECTED["player"]
            playerselect[2] = SELECTED["notplayer"]
            playerselect[3] = SELECTED["notplayer"]
        if int(elemento_inicial) == 3:
            playerselect[0] = SELECTED["notplayer"]
            playerselect[1] = SELECTED["notplayer"]
            playerselect[2] = SELECTED["player"]
            playerselect[3] = SELECTED["notplayer"]
        if int(elemento_inicial) == 4:
            playerselect[0] = SELECTED["notplayer"]
            playerselect[1] = SELECTED["notplayer"]
            playerselect[2] = SELECTED["notplayer"]
            playerselect[3] = SELECTED["player"]


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
        
        print(x)
        elemento_inicial = input("\nSelecione outra cartela (2,3 ou 4) ou pressione ENTER para sortear\n")
        if elemento_inicial == "1" or elemento_inicial == "2" or elemento_inicial == "3" or elemento_inicial == "4":
            os.system("cls || clear")
        else:
            os.system("cls || clear")
            print(f'{ERRORS["invalid"]}\nValores suportados são [1, 2, 3, 4, ENTER]\n')
            elemento_inicial = 1

TUI_principal(1)