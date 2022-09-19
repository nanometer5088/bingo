import os
def idioma():
    #Apresenta idiomas disponíveis ao usuário
    os.system("cls || clear")
    x = input("""

    Selecione seu idioma
    Select your language

    1 = Português Brasileiro
    2 = English
    """)
    if x == "1":
        return "BR"
    elif x == "2":
        return "EN"
    else:
        return ""

def tutorial(locale):
    #Tutorial - Busca as informações do constants.py e apresenta na tela em
    #formato 'apresentação de slides'
    os.system("cls || clear")
    input(locale.INTRO["intro1"])
    os.system("cls || clear")
    input(locale.INTRO["intro2"])
    os.system("cls || clear")
    input(locale.INTRO["intro3"])
    os.system("cls || clear")
    input(locale.INTRO["intro4"])
    os.system("cls || clear")
    input(locale.INTRO["intro5"])
    os.system("cls || clear")
    input(locale.INTRO["introfinal"])
    os.system("cls || clear")

def inicio(locale):
    #Início do programa e indrodução para o usuário
    os.system("cls || clear")
    x = input(locale.START["intro"])

    #Verifica por atualizações, e avisa o usuário caso encontre alguma
    try:
        import requests
        data = requests.get("https://raw.githubusercontent.com/nanometer5088/bingo/main/VERSION")
        version = open('VERSION', 'r', encoding='utf=8')
        if version.readline().rstrip() < (data.text):
            os.system("cls || clear")
            input(locale.WARNING["newversion"])
    except requests.exceptions.ConnectionError:
        print()
    
    #Detecção e instalação das dependências - Caso não estejam instaladas,
    #a instalação ocorre e o programa é encerrado. O usuário é avisado para reiniciar
    #o programa ao finalizar
    try:
        from prettytable import PrettyTable
        from colr import color
    except ModuleNotFoundError:
        os.system("cls || clear")
        input(locale.START["libraries"])
        os.system("pip install -r requirements.txt --user")
        os.system("cls || clear")
        return "instalado"
    #Buscar arquivo de configuração - Caso não encontrado, ele é criado e 
    # o jogador é apresentado com a opção de ver o tutorial
    try:
        config = open('config.json', 'r', encoding='utf-8')
        config.close()
    except FileNotFoundError:
        config = open('config.json', 'w')
        config.write('Tutorial_Done=1')
        config.close()
        os.system("cls || clear")
        resposta = input(locale.WARNING["firstime"])
        if resposta == "":
            tutorial(locale)
        elif resposta == "1":
            os.system("cls || clear")
            input(locale.WARNING["firsttimeskip"])