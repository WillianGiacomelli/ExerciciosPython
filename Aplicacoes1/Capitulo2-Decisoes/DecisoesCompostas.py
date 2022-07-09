nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper()

if idade >= 65 :
    print("O paciente " + nome + "  possui atendimento prioritário?")
elif doenca_infectocontagiosa == "SIM" :
    print("O paciente " + nome + " deve ser levado para outra sala")
else :
    print("O paciente " + nome + " Não possui atendimento prioritário")