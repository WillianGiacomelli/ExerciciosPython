# Reduce -  recebe uma lista e retorna um único valor para essa lista

from functools import reduce

def soma(x,y):
    return x+y

lista = [1,3,5,6,7,8,9,10]

soma = reduce(soma,lista)
print(soma)