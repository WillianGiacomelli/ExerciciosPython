#Programa que compara 2 sequências de aminoacidos diferentes
def comparaSequencia(seq1, seq2):
    if seq1 == seq2:
        print("As sequência são iguais")
        return 0
    else:
        print("As sequências são diferentes")


sequencia1 = input("Entre com a sequência de aminoácidos: ").upper()
sequencia2 = input("Entre com a outra sequência de aminoácidos: ").upper()

comparaSequencia(sequencia1, sequencia2)
