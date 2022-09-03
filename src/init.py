import os
def tutorial():
    #Tutorial - Busca as informações do constants.py e apresenta na tela em
    #formato 'apresentação de slides'
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
    #Início do programa e indrodução para o usuário
    from src.constants import WARNING, START
    os.system("cls || clear")
    x = input(START["intro"])
    #Detecção e instalação das dependências - Caso não estejam instaladas,
    #a instalação ocorre e o programa é encerrado. O usuário é avisado para reiniciar
    #o programa ao finalizar
    try:
        from prettytable import PrettyTable
        from colr import color
    except ModuleNotFoundError:
        os.system("cls || clear")
        input(START["libraries"])
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
        resposta = input(WARNING["firstime"])
        if resposta == "":
            tutorial()
        elif resposta == "1":
            os.system("cls || clear")
            input(WARNING["firsttimeskip"])