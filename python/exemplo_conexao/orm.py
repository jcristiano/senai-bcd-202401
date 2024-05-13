from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'aluno'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    data_nascimento = Column(Date, name='nascimento')

def calcular_idade(data_nascimento):
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Criar engine e criar tabelas no banco de dados
engine = create_engine('mysql+mysqlconnector://app_python:apppython@localhost/myapp')
Base.metadata.create_all(engine)

# Criar sessão
Session = sessionmaker(bind=engine)
session = Session()

# Exemplo de uso
data_nascimento = datetime(2000, 5, 15)
aluno = Aluno(nome='João', data_nascimento=data_nascimento)
session.add(aluno)
session.commit()

# Recuperar o aluno do banco de dados
aluno_recuperado = session.query(Aluno).filter_by(nome='João').first()
idade_aluno = calcular_idade(aluno_recuperado.data_nascimento)
print(f"A idade do aluno é: {idade_aluno} anos")

# Fechar a sessão
session.close()
