import random

def aleatorio(x, y):
#Retorna um valor aleatório de tamanho a ser determinado
    return random.randint(x, y)

def geralistaaleatoria(x, y):
    #Gera uma lista de números à serem sorteados - Esses números são
    #únicos e aleatórios.
    return random.sample(range(x), k=y)