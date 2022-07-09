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

equipamentoD=input("Digite o nome do equipamento a ser depreciado:").upper()
for indice in range(0,len(equipamento)):
    if equipamento[indice]==equipamentoD:
        print("Valor antigo:",valor[indice])
        valor[indice] == valor[indice]*0.9
        print("ValorNovo:",valor[indice])
