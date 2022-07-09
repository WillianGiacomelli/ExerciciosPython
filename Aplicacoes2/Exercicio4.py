#Algoritmo que ordena lista numérica de acordo com o tamanho dos números

l = []

x = 0

while x <=  2:
    n = int(input("Entre com o número na lista: "))
    l.append(n)
    x = x + 1


ordenada = sorted(l)

print(l)
print(ordenada)



