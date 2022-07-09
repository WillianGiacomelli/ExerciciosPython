#Zip - Concatena diferentes listas

lista1 = [1,2,3]
lista2 = ["Camisa","Blusa","Camiseta"]
lista3 = ["R$99,90","R$199,90","R$59,90"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)