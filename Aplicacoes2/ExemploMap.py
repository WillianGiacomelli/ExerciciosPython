#Map - Aplica determinada função a cada item de uma lista

def dobro(x):
    return x*2

lista = [1,2,3,4,5,6]

lista_dobrada = map(dobro, lista)

lista_dobrada = list(lista_dobrada)
print(lista_dobrada)

