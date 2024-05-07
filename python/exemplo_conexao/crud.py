from mysql import connector as MyConnector

def criar_tabela_aluno(conexao):
    sql = """
        CREATE TABLE IF NOT EXISTS aluno (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            nascimento DATE
        )
    """
    cursor = conexao.cursor()
    cursor.execute(sql)
    cursor.close()

def criar_novo_aluno(conexao):
    nome = input("Digite o nome do aluno: ")
    nascimento = input("Digite o nascimento no formado dd/mm/YYYY: ")
    nascimento_mysql = '-'.join(nascimento.split('/')[::-1])

    cursor = conexao.cursor()
    sql = "INSERT INTO aluno (nome, nascimento) VALUES (%s, %s)"
    cursor.execute(sql, (nome, nascimento_mysql))
    conexao.commit()
    cursor.close()

if __name__ == "__main__":
    try:
        conexao = MyConnector.connect(
            host='localhost',
            user='myapp',
            password='myapp',
            database='mydbpython',
            port=3306,
        )

        if conexao.is_connected:
            print('Conexao estabelecida')

            criar_tabela_aluno(conexao)
            criar_novo_aluno(conexao)
            conexao.close()
    except MyConnector.Error as err:
        print("Erro ao conectar ao MySQL: {0}".format(err))
