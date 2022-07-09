#Programa que recebe arquivo e faz leitura

w = open("contatos.txt", "w")

w.write("Juliano: 19 - 987006425")

w.close()

arquivo = open("contatos.txt")

texto = arquivo.read()

print(texto)

arquivo.close()

