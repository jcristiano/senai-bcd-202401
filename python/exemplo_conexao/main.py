from mysql import connector as MyConnector
from datetime import datetime


def tabela_existe(conexao: MyConnector, nome_tabela: str) -> bool:
    cursor = conexao.cursor()
    cursor.execute("SHOW TABLES LIKE %s", (nome_tabela,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado is not None

def criar_tabela_aluno(conexao):
    if not tabela_existe(conexao, "aluno"):
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS aluno  (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome varchar(255),
                nascimento DATE
            )
        """)

def calcular_idade(data_nascimento):
    # Obter a data atual
    data_atual = datetime.now()

    # Calcular a diferença entre a data atual e a data de nascimento
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

    return idade

def criar_aluno(conexao):
    nome = input("Digite o nome do aluno: ")
    nascimento = input("Digite a data de nascimento do aluno (formato dd/mm/YYYY): ")
    nascimento_mysql = '-'.join(nascimento.split('/')[::-1])
    
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO aluno (nome, nascimento ) VALUES (%s, %s)", (nome, nascimento_mysql,))
    conexao.commit()
    cursor.close()
    print("Aluno {0} inserido com sucesso. Value {1}".format(nome, nome))


def listar_alunos(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT 
            a.id, 
            a.nome, 
            a.nascimento 
        FROM aluno a
    """)
    alunos = cursor.fetchall()
    for aluno in alunos:
        fmtAluno = "A entrada {0} corresponde ao aluno(a) {1}. A pessoa nasceu em {2} e tem a idade de {3}"      
        print(fmtAluno.format(aluno[0], aluno[1], aluno[2], calcular_idade(aluno[2])))

def atualizar_aluno(conexao):
    id_aluno = int(input("Digite o ID do aluno que deseja atualizar: "))
    nome = input("Digite o novo nome do aluno: ")
    idade = int(input("Digite a nova idade do aluno: "))
    cursor = conexao.cursor()
    cursor.execute("UPDATE aluno SET nome = %s, idade = %s WHERE id = %s", (nome, idade, id_aluno))
    conexao.commit()
    print("Aluno atualizado com sucesso.")

def excluir_aluno(conexao):
    id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM aluno WHERE id = %s", (id_aluno,))
    conexao.commit()
    print("Aluno excluído com sucesso.")        

def menu_alunos(conexao: MyConnector) -> None:
    exibir_menu = True
    while exibir_menu:
        print("\nMenu:")
        print("1. Criar aluno")
        print("2. Listar alunos")
        print("3. Atualizar aluno")
        print("4. Excluir aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_aluno(conexao)
        elif opcao == "2":
            listar_alunos(conexao)
        elif opcao == "3":
            print("Atualizar aluno")
        elif opcao == "4":
            print("Excluir aluno")
        elif opcao == "5":
            exibir_menu = False
        else:
            print("Opcao invalida. Tente novamente.")

#main
if __name__ == "__main__":
    conexao = MyConnector.connect(
        host="localhost",
        user="app_python",
        password="App@Senai@20240505",
        database="myapp"
    )

    if conexao.is_connected:
        print('conexao estabelecida')
        criar_tabela_aluno(conexao)
        menu_alunos(conexao)
        conexao.close()


    print('Executado método main')