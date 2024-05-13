import mysql.connector

class ConexaoMySQL:

    _conexao = None

    @staticmethod
    def obter_conexao(host, usuario, senha, banco):

        if ConexaoMySQL._conexao is None or not ConexaoMySQL._conexao.is_connected():
            ConexaoMySQL._conexao = mysql.connector.connect(
                host=host,
                user=usuario,
                password=senha,
                database=banco
            )
        return ConexaoMySQL._conexao
    
    @staticmethod
    def fechar_conexao():
        if ConexaoMySQL._conexao is None or not ConexaoMySQL._conexao.is_connected():
            ConexaoMySQL._conexao.close()
            ConexaoMySQL._conexao = None