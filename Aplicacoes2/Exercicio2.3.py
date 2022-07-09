#Programa que recebe uma sequencia digitada pelo usuário e salva em um formato fasta

seq = input("Entre com a sequência para o arquivo: ")

nome_arquivo = input("Entre com o nome que deseja para o arquivo: ")

arquivo = open(nome_arquivo + ".fasta", "w")

arquivo.write(seq)

arquivo.close()