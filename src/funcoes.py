def aleatorio(x, y):
#Retorna um valor aleatório de tamanho a ser determinado
    import random
    return random.randint(x, y)

def geralistaaleatoria():
    #Gera uma lista de números à serem sorteados - Esses números são
    #únicos e aleatórios, entre 0 e 50
    import random
    x = random.sample(range(50), k=50)
    return x