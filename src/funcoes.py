def aleatorio(x, y):
    import random
    return random.randint(x, y)

def criaarquivo():
    try:
        arquivo = open('temp.json', 'r', encoding='utf-8')
        arquivo.close()
    except FileNotFoundError:
        arquivo = open('temp.json', 'w')
        arquivo.close()

def learquivo(x,linha):
    criaarquivo()
    arquivo = open(x, 'r', encoding='utf-8')
    x = arquivo.readlines(linha)
    arquivo.close()
    return x

def escrevearquivo(x,input):
    criaarquivo()
    arquivo = open(x, 'w')
    arquivo.write(input)
    arquivo.close()

def cleanup():
    import os
    if os.path.exists("temp.json"):
        os.remove("temp.json")
    else:
        print("The file does not exist\n")

