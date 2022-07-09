#Filter -  função que utiliza outra função para filtrar uma lista

def pares(i):
    if i % 2 == 0:
        return i


lista = [1,2,3,4,5,6,7,8,9,10]

lista_pares = filter(pares, lista)
print(list(lista_pares)) #list é uma função que converte um objeto em uma lista