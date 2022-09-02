TUTORIAL = {
    "start": """
    Projeto: Bingo Lite
    Algoritmos e Programação II - Turma 02D
    Segundo semestre - 2022


    Certifique-se que tenha as bibliotecas necessárias instaladas

    As bibliotecas podem ser instaladas rodando o arquivo 'setup.py'

    Pressione ENTER para prosseguir
    """
    }
SELECTED = {
    "player": "■",
    "notplayer": " "
    }
ERRORS = {
    "invalid": "Valor de entrada inválido"
}

DEPRECATED = {
    "TUI-without-prettytable": '''
        while elemento_inicial == 1 or elemento_inicial == 2 or elemento_inicial == 3 or elemento_inicial == 4:
        if elemento_inicial == 1:
            elemento_inicial = int(input(f"""
            Cartela 1: {lista[0][1]} {SELECTED["player"]}
            Cartela 2: {lista[1][1]} 
            Cartela 3: {lista[2][1]} 
            Cartela 4: {lista[3][1]} 
            """))
        elif elemento_inicial == 2:
            elemento_inicial = int(input(f"""
            Cartela 1: {lista[0][1]} 
            Cartela 2: {lista[1][1]} {SELECTED["player"]}
            Cartela 3: {lista[2][1]} 
            Cartela 4: {lista[3][1]} 
            """))
        elif elemento_inicial == 3:
            elemento_inicial = int(input(f"""
            Cartela 1: {lista[0][1]} 
            Cartela 2: {lista[1][1]} 
            Cartela 3: {lista[2][1]} {SELECTED["player"]}
            Cartela 4: {lista[3][1]} 
            """))
        elif elemento_inicial == 4:
            elemento_inicial = int(input(f"""
            Cartela 1: {lista[0][1]} 
            Cartela 2: {lista[1][1]} 
            Cartela 3: {lista[2][1]} 
            Cartela 4: {lista[3][1]} {SELECTED["player"]}
            """))
        os.system("cls || clear")
        elif elemento_inicial == '':
            aleatorio(1, 5)
            '''
    }