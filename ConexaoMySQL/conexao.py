import mysql.connector
from mysql.connector import errorcode

def selecionar():
    ra = input("Entre com o RA do aluno a ser selecionado: ")

    cursor = db_connection.cursor()
    sql = "select ra,nome,cpf from aluno where ra = %s"
    values = [ra]
    cursor.execute(sql, values)

    for (ra, nome, cpf) in cursor:
        print(ra, nome, cpf)
        print("\n")

    cursor.close()
    db_connection.commit()
    db_connection.close()

    return 0



def inserir():
    nome = input("Entre com o nome do aluno a ser inserido: ")
    cpf = input("Entre com o CPF do aluno: ")

    if (nome and cpf):
            cursor = db_connection.cursor()
            sql = "INSERT INTO aluno (nome, cpf) VALUES (%s, %s)"
            values = (nome, cpf)
            cursor.execute(sql, values)

            print(cursor.rowcount, "Registro inserido.")
            print("\n")

            for (ra, nome, cpf) in cursor:
                print(ra, nome, cpf)
            print("\n")
            
            cursor.close()
            db_connection.commit()
            db_connection.close()
    else:
            print("Dados não foram digitados")
            quit()
            
    return 0

def atualizar():
    ra = input("Entre com o RA do aluno a ser atualizado: ")
    nome = input("Entre com o Nome do aluno a ser atualizado: ")
    cpf = input("Entre com o CPF do aluno a ser atualizado: ")

    cursor = db_connection.cursor()
    sql = "update aluno set nome = %s, cpf = %s where ra=%s"
    values = [nome,cpf,ra]
    cursor.execute(sql, values)

    for (id, name, cpf) in cursor:
        print(id, name, cpf)
        print("\n")

    return 0


def deletar():
    ra = input("Entre com o RA do aluno a ser deletado: ")

    cursor = db_connection.cursor()
    sql = "delete from aluno where ra = %s"
    values = [ra]
    cursor.execute(sql, values)

    return 0

try:
	db_connection = mysql.connector.connect(host='localhost', user='root', password='root', database='escola')
	print("Conexão feita!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Base de dados não existe")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Usuário ou senha errados")
	else:
		print(error)
else:

    opcao = 0

    while opcao != 5:

        print("Menu\n")

        print("1 - Selecionar dados")
        print("2 - Inserir dados")
        print("3 - Atualizar dados")
        print("4 - Deletar dados")
        print("5 - Sair")


        opcao = int(input("\n Escolha a opção:"))

        if opcao == 1:
            selecionar()

        elif opcao == 2:
            inserir()

        elif opcao == 3:
            atualizar()

        elif opcao == 4:
            deletar()

        elif opcao == 5:
            quit()



   
  
    