def aleatorio(x, y):
    import random
    return random.randint(x, y)

def criaarquivo(x):
    try:
        arquivo = open(x, 'r', encoding='utf-8')
        arquivo.close()
    except FileNotFoundError:
        arquivo = open(x, 'w')
        arquivo.close()

def learquivo(x,linha):
    criaarquivo(x)
    arquivo = open(x, 'r', encoding='utf-8')
    x = arquivo.readlines(linha)
    arquivo.close()
    return x

def escrevearquivo(x,input):
    criaarquivo(x)
    arquivo = open(x, 'w')
    arquivo.write(input)
    arquivo.close()

def cleanup(x):
    import os
    if os.path.exists(x):
        os.remove(x)
    else:
        print("The file does not exist\n")

