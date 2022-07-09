#Programa menu com funções diferentes


def abrirArquivo():
    nomearquivo = print("Entre com nome do arquivo que deseja ler: ")
    arquivo = open(nomearquivo)
    return arquivo

def lerArquivo(arquivo):
    linhas = arquivo.readLines()

    for linha in linhas:
        print(linha)


opcao = 0

while opcao != 3:
    print(" Menu de funções")
    print("1 - Ler arquivo")
    print("2 - Mostrar conteúdo do arquivo")
    print("3 - Fechar programa")
    opcao = int(input("Entre com a função que deseja utilizar: "))

    if opcao == 1:
        arquivo = abrirArquivo()

    elif opcao ==2:
        lerArquivo(arquivo)

    else:
        quit()

