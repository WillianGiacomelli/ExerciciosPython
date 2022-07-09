#Calculadora de raizes de uma equeção de segundo grau

a = int(input("Entre com o valor para a: "))
b = int(input("Entre com o valor para b: "))
c = int(input("Entre com o valor para c: "))

delta = b**2 - 4*a*c
x1 = (-b + delta**(1/2))/ (2*a)
x2 = (-b - delta**(1/2))/ (2*a)

print(" O valor da primeira raiz é:", x1)
print(" O valor da segunda raiz é:" + str(x2))
