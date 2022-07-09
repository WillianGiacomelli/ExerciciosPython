equipamento=[]
valor=[]
serial=[]
departamento=[]

resposta="S"

while resposta=="S":
    equipamento.append(input("Equipamento:").upper())
    valor.append(float(input("Valor: ")))
    serial.append(int(input("Número serial:")))
    departamento.append(input("Departamento: "))
    resposta=input("Digite 'S' para continuar:")

serialDanificado = input("Digite o número serial do aparelho a ser deletado")
for indice in range(0,len(serial)):
    if serial[indice]==serialDanificado:
        del serial[indice]
        del equipamento[indice]
        del departamento[indice]
        del valor[indice]
        break

for resul in serial:
    print(serial)