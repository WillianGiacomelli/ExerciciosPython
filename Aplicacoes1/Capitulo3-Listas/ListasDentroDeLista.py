inventario=[]
resposta="S"

while resposta=="S":
    equipamento=[input("Equipamento: "),
            float(input("Valor: ")),
            int(input(("Número serial: "))),
            input("Departamento: ")]
    inventario.append(equipamento)
    resposta=input("Digite S para continuar").upper()

for elemento in inventario:
    print("Nome:", elemento[0])
    print("Valor:",elemento[1])
    print("Serial:",elemento[2])
    print("Departamento",elemento[3])

busca=input("Entre com o equipamento que deseja buscar")
for elemento in inventario:
     if busca==elemento[0]:
         print("Valor:",elemento[1])
         print("Serial",elemento[2])

depreciacao=input("Digite o nome do produto a ser depreciado")
for elemento in inventario:
    if depreciacao==elemento[0]:
        print("Valor antes do ajuste",elemento[1])
        elemento[1]=elemento[1]*0.90
        print("Valor depois do ajuste",elemento[1])

serial=int(input("Digite o serial do produto a ser excluido:"))
for elemento in inventario:
    if elemento[2]==serial:
        inventario.remove(elemento)

valores=[]
for elemento in inventario:
    valores.append(elemento[1])

if len(valores)>0:
    print("Equipamento mais caro custa:", max(valores))
    print("Equipamento mais barato custa:", min(valores))
    print("O total de equipamentos é:", sum(valores))