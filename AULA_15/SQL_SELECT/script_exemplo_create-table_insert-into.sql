/* ----- ------ EXEMPLO - CREATE DATABASE, CREATE TABLE E INSERT INTO ------ ------ */
CREATE DATABASE bd_exemplo_aula_01;

USE bd_exemplo_aula_01;

CREATE TABLE produtos (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL
);

/* CADASTRAR NA TABELA */
INSERT INTO produtos (produto, valor, quantidade)
VALUES ('Arroz 5kg', 25.00, 120);

INSERT INTO produtos (produto, valor, quantidade)
VALUES ('Feijao 1kg', 10.00, 80);

INSERT INTO produtos (produto, valor, quantidade) VALUES
('Macarrao 500g', 5.00, 150),
('Oleodesoja 900ml', 7.50, 70),
('Acucar 1kg', 4.00, 100);



/* ----- ------ ATIVIDADE - CREATE DATABASE, CREATE TABLE E INSERT INTO ------ ------ */
CREATE DATABASE bd_clientes;

USE bd_clientes;

CREATE TABLE tb_clientes (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    idade INT NOT NULL
);

INSERT INTO tb_clientes (nome, email, idade)
VALUES ('Maria Silva', 'maria@email.com', 28);


INSERT INTO tb_clientes (nome, email, idade) VALUES
('João Santos', 'joao@email.com', 35),
('Ana Costa', 'ana@email.com', 22);


SELECT * FROM tb_clientes;