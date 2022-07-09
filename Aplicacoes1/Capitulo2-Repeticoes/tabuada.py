numero = int(input("Digite o número da tabuada desejada:"))


for contador in range(0,11,1):
    print(str(numero) + "X" + str(contador) + "=" + str(contador*numero))

