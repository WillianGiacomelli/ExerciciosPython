equipamento=[]
valor=[]
serial=[]
departamento=[]

resposta="S"

while resposta=="S":
    equipamento.append(input("Equipamento:"))
    valor.append(float(input("Valor: ")))
    serial.append(int(input("Número serial:")))
    departamento.append(input("Departamento: "))
    resposta=input("Digite 'S' para continuar:")

for indice in range(0,len(equipamento)):
    print("Equipamento:", (indice+1))
    print("Nome:", equipamento[indice])
    print("Valor:", valor[indice])
    print("Serial:", serial[indice])
    print("Departamento:", departamento[indice])

busca=input("Digite o nome do equipamento que deseja buscar:")
for indice in range(0,len(equipamento)):
    if busca==equipamento[indice]:
        print("Valor:", valor[indice])
        print("Serial:", serial[indice])
