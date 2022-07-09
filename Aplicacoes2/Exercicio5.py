#Exercicio de operação matemática com números

operacao = input("Entre com a operação: ")

n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segundo número: "))

if operacao == "+":
    soma = n1 + n2
    print("O resultado da soma é" + str(soma))
elif operacao == "-":
    subtracao = n1 - n2
    print("O resultado da subtração é ",subtracao)
elif operacao == "*":
    multiplicacao = n1 * n2
    print("O resultado da multiplicação é " + str(multiplicacao))
else:  
    divisao = n1/n2
    print("O resultado da divisão é: " + str(divisao))
