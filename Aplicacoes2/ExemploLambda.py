#Lambda - tipo de função que será executada apenas uma vez. Geralmente associada a Map


lista = [1,2,3,4,5,6]

lista_dobrada = map(lambda i: i*2, lista)

lista_dobrada = list(lista_dobrada)
print(lista_dobrada)