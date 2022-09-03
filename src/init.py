import os
def tutorial():
    from src.constants import INTRO
    os.system("cls || clear")
    input(INTRO["intro1"])
    os.system("cls || clear")
    input(INTRO["intro2"])
    os.system("cls || clear")
    input(INTRO["intro3"])
    os.system("cls || clear")
    input(INTRO["intro4"])
    os.system("cls || clear")
    input(INTRO["intro5"])
    os.system("cls || clear")
    input(INTRO["introfinal"])
    os.system("cls || clear")

def inicio():
    from src.constants import WARNING, START
    os.system("cls || clear")
    x = input(START["intro"])
    try:
        from prettytable import PrettyTable
        from colr import color
    except ModuleNotFoundError:
        os.system("cls || clear")
        input(START["libraries"])
        os.system("pip install -r requirements.txt --user")
        os.system("cls || clear")
        return "instalado"
    try:
        config = open('config.json', 'r', encoding='utf-8')
        config.close()
    except FileNotFoundError:
        config = open('config.json', 'w')
        config.write('Tutorial_Done=1')
        config.close()
        os.system("cls || clear")
        resposta = input(WARNING["firstime"])
        if resposta == "":
            tutorial()
        elif resposta == 1:
            print()