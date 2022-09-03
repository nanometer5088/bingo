from src.constants import START, WARNING, ERRORS
import os

def tutorial():
    os.system("cls || clear")
    input(START["intro1"])
    os.system("cls || clear")
    input(START["intro2"])
    os.system("cls || clear")
    input(START["intro3"])
    os.system("cls || clear")

def inicio():
    os.system("cls || clear")
    x = input(START["intro"])
    os.system("pip install -r requirements.txt")
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
        else:
            print(ERRORS["invalid"],"Valores possíveis sáo: ENTER, 1")