# Exemplo de aplicação Enumerate

lista = ["abacate", "abacaxi", "morango"]

#sem enumerate
#for i in range(len(lista)):
#   print(i, lista[i]);

#com enumerate

for i, nome in enumerate(lista):
    print(i, nome)
