import random

def aleatorio(min, max):
#Retorna um valor aleatório de tamanho a ser determinado
    return random.randint(min, max)

def geralistaaleatoria(max, quantelementos):
    #Gera uma lista de números à serem sorteados - Esses números são
    #únicos e aleatórios.
    return random.sample(range(max), k=quantelementos)