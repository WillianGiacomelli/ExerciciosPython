# Algoritmo que recebe duas notas e diga se o usuário foi aprovado se a nota for >= 6

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))

media = (nota1 + nota2)/2

if media >= 6:
    print("O aluno foi aprovado")
else:
    print("O aluno não foi aprovado")

