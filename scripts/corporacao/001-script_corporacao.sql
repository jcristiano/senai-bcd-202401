DROP DATABASE IF EXISTS corporacao;

CREATE DATABASE corporacao;

USE corporacao;

CREATE TABLE departamento (
    codigo INT AUTO_INCREMENT,
    nome VARCHAR(100) 
		NOT NULL,
	CONSTRAINT 
		pk_depto_codigo PRIMARY KEY (codigo)
);


CREATE TABLE funcionario (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nascimento DATE,
    cargo VARCHAR(100),
    salario DECIMAL(10, 2),
    departamento INT NOT NULL,
	CONSTRAINT fk_funcionario_depto_codigo
    FOREIGN KEY (departamento) REFERENCES departamento(codigo)
);

CREATE TABLE dependente (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    relacionamento ENUM('Filho', 'Filha', 'Esposa', 'Marido', 'Pai', 'Mãe', 'Outro'),
    funcionario INT,
    FOREIGN KEY (funcionario) REFERENCES funcionario(codigo)
);


INSERT INTO departamento (nome) VALUES
('Recursos Humanos'),
('Financeiro'),
('Tecnologia da Informação'),
('Vendas');

INSERT INTO funcionario (nome, nascimento, cargo, salario, departamento) VALUES
('João Silva', '1980-05-15', 'Analista de RH', 4500.00, 1),
('Maria Oliveira', '1985-10-20', 'Contador', 5000.00, 2),
('Pedro Santos', '1990-03-25', 'Programador', 5500.00, 3),
('Ana Souza', '1982-07-12', 'Vendedora', 4000.00, 4),
('Marcos Pereira', '1987-09-30', 'Analista de RH', 4800.00, 1),
('Juliana Costa', '1988-12-05', 'Analista Financeiro', 5200.00, 2),
('Lucas Oliveira', '1993-02-18', 'Desenvolvedor Web', 6000.00, 3),
('Fernanda Silva', '1978-04-22', 'Gerente de Vendas', 6500.00, 4),
('Rodrigo Santos', '1984-06-28', 'Recrutador', 4700.00, 1),
('Mariana Gonçalves', '1989-08-07', 'Analista Contábil', 5200.00, 2),
('Gustavo Almeida', '1992-11-11', 'Analista de Sistemas', 5800.00, 3),
('Carla Lima', '1975-01-14', 'Representante Comercial', 4500.00, 4),
('Rafaela Ferreira', '1983-03-03', 'Especialista em Treinamento', 4900.00, 1),
('Luciano Costa', '1995-07-08', 'Analista Financeiro', 5200.00, 2),
('Bianca Santos', '1986-09-19', 'Desenvolvedora Full Stack', 6200.00, 3),
('Marcelo Oliveira', '1977-11-24', 'Gerente de Contas', 6800.00, 4),
('Camila Rodrigues', '1981-12-31', 'Especialista em Benefícios', 5000.00, 1),
('Ricardo Alves', '1989-02-05', 'Contador', 5300.00, 2),
('Patrícia Lima', '1991-04-17', 'Analista de Banco de Dados', 5700.00, 3),
('Luiz Fernandes', '1980-06-26', 'Vendedor', 4200.00, 4);

-- Inserindo 5 dependentes
INSERT INTO dependente (nome, relacionamento, funcionario) VALUES
('Ana Carolina Silva', 'Filha', 1),
('José Silva', 'Pai', 1),
('Mateus Oliveira', 'Filho', 3),
('Fernanda Pereira', 'Esposa', 5),
('Pedro Costa', 'Pai', 8);
