-- SELECT * FROM TB_EMPRESTIMOS;
-- SELECT * FROM TB_LIVROS;
-- SELECT * FROM TB_USUARIOS;

ALTER TABLE tb_usuarios
MODIFY COLUMN id_usuario INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_usuario);

ALTER TABLE tb_livros
MODIFY COLUMN id_livro INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_livro);


ALTER TABLE tb_emprestimos
MODIFY COLUMN id_emprestimo INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_emprestimo);


ALTER TABLE tb_itens_emprestados
MODIFY COLUMN id_item INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_item);



ALTER TABLE tb_emprestimos
ADD CONSTRAINT fk_usuario
FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario);


ALTER TABLE tb_itens_emprestados
ADD CONSTRAINT fk_livro
FOREIGN KEY (id_livro) REFERENCES tb_livros(id_livro);


ALTER TABLE tb_itens_emprestados
ADD CONSTRAINT fk_emprestimo
FOREIGN KEY (id_emprestimo) REFERENCES tb_emprestimos(id_emprestimo);




-- MOSTRAR OS IDs DE LIVROS QUE NÃO ESTÃO NA TB_LIVROS, MAS ESTÃO NO EMPRÉSTIMOS (SE ACONTECER ISSO, GERA UM ERRO)
SELECT * FROM tb_itens_emprestados 
WHERE id_livro NOT IN (SELECT id_livro FROM tb_livros);



/*MÃO NA MASSA*/
-- 
SELECT tb_livros.titulo
FROM tb_livros, tb_itens_emprestados
WHERE tb_livros.id_livro = tb_itens_emprestados.id_livro;

-- Mostre a data de cada empréstimo e o título do livro emprestado.
SELECT tb_emprestimos.data_emprestimo, tb_livros.titulo
FROM tb_emprestimos, tb_itens_emprestados, tb_livros
WHERE tb_emprestimos.id_emprestimo = tb_itens_emprestados.id_emprestimo
  AND tb_livros.id_livro = tb_itens_emprestados.id_livro;

-- Mostre os livros emprestados
SELECT tb_livros.titulo, tb_livros.valor_emprestimo
FROM tb_livros, tb_itens_emprestados
WHERE tb_livros.id_livro = tb_itens_emprestados.id_livro;

-- Quais livros foram emprestados no dia 2024-10-15?
SELECT tb_livros.titulo
FROM tb_livros, tb_itens_emprestados, tb_emprestimos
WHERE tb_livros.id_livro = tb_itens_emprestados.id_livro
  AND tb_emprestimos.id_emprestimo = tb_itens_emprestados.id_emprestimo
  AND tb_emprestimos.data_emprestimo = '2024-10-15';


/* **** EXEMPLOS DE JOIN ****/
-- Mostrar o nome dos usuários e a data dos empréstimos
SELECT 
  tb_usuarios.nome,
  tb_emprestimos.data_emprestimo
FROM 
  tb_usuarios
JOIN 
  tb_emprestimos ON tb_usuarios.id_usuario = tb_emprestimos.id_usuario;

-- Mostrar os nomes dos livros que foram emprestados e os códigos dos empréstimos
SELECT 
  tb_livros.titulo,
  tb_itens_emprestados.id_emprestimo
FROM 
  tb_livros
JOIN 
  tb_itens_emprestados ON tb_livros.id_livro = tb_itens_emprestados.id_livro;


/* ************ JOINS MAIORES **************** */
-- JUNTA CLIENTES, PEDIDOS, ITENS E PRODUTOS PARA MOSTRAR QUEM COMPROU O QUÊ E EM QUAL DATA.
SELECT
    tb_clientes.nome,
    tb_pedidos.data_pedido,
    tb_produtos.produto
FROM tb_pedidos
INNER JOIN tb_clientes
    ON tb_pedidos.cliente_codigo = tb_clientes.cod_cliente
INNER JOIN tb_itens
    ON tb_pedidos.codigo_pedido = tb_itens.pedido_codigo
INNER JOIN tb_produtos
    ON tb_itens.item_codigo = tb_produtos.codigo_produto;

-------------------------------------------------------------------------
-- OUTROS JOINS DE EXEMPLO

-- 1 JOIN: emprestimos -> usuarios
-- Resultado: nome do usuário + data de devolução

SELECT
    tb_usuarios.nome,
    tb_emprestimos.data_devolucao
FROM tb_emprestimos
INNER JOIN tb_usuarios
    ON tb_usuarios.id_usuario = tb_emprestimos.id_usuario;


-- Junta empréstimos com itens de empréstimo
-- Objetivo: descobrir quais livros foram pegos em cada empréstimo

SELECT
    tb_emprestimos.id_emprestimo,
    tb_livros.titulo
FROM tb_emprestimos
INNER JOIN tb_itens_emprestimos
    ON tb_itens_emprestimos.id_emprestimo = tb_emprestimos.id_emprestimo
INNER JOIN tb_livros
    ON tb_livros.id_livro = tb_itens_emprestimos.id_livro;


-- Junta usuário + empréstimo + item + livro
-- Objetivo: mostrar QUEM pegou QUAL LIVRO

SELECT
    tb_usuarios.nome,              -- Quem pegou
    tb_emprestimos.id_emprestimo,  -- Empréstimo
    tb_livros.titulo               -- Nome do livro pegado
FROM tb_usuarios
INNER JOIN tb_emprestimos
    ON tb_emprestimos.id_usuario = tb_usuarios.id_usuario
INNER JOIN tb_itens_emprestimos
    ON tb_itens_emprestimos.id_emprestimo = tb_emprestimos.id_emprestimo
INNER JOIN tb_livros
    ON tb_livros.id_livro = tb_itens_emprestimos.id_livro;


-- ----------------------------------------------------------------------
-- TOTALIZAR OS VALORES POR EMPRÉSTIMO E MOSTRAR OS IDS DOS EMPRÉSTIMOS
SELECT 
  tb_itens_emprestados.id_emprestimo,
  SUM(tb_livros.valor_emprestimo) AS total_emprestimo
FROM 
  tb_itens_emprestados
JOIN 
  tb_livros ON tb_itens_emprestados.id_livro = tb_livros.id_livro
GROUP BY 
  tb_itens_emprestados.id_emprestimo
ORDER BY 
  tb_itens_emprestados.id_emprestimo;


-- MOSTRAR OS CLIENTES QUE ALUGARAM, AS DATAS DOS ALUGUÉIS E OS TOTAIS DE CADA CLIENTE
SELECT 
  tb_usuarios.id_usuario,
  tb_usuarios.nome,
  tb_emprestimos.data_emprestimo,
  SUM(tb_livros.valor_emprestimo) AS total_livros
FROM 
  tb_itens_emprestados
JOIN 
  tb_livros ON tb_itens_emprestados.id_livro = tb_livros.id_livro
JOIN 
  tb_emprestimos ON tb_itens_emprestados.id_emprestimo = tb_emprestimos.id_emprestimo
JOIN 
  tb_usuarios ON tb_emprestimos.id_usuario = tb_usuarios.id_usuario
GROUP BY 
  tb_usuarios.id_usuario,
  tb_usuarios.nome, 
  tb_emprestimos.data_emprestimo
ORDER BY 
  tb_usuarios.id_usuario,
  tb_emprestimos.data_emprestimo;


/*
-- APELIDOS NO JOIN
SELECT 
  ie.id_emprestimo,
  SUM(l.valor_emprestimo) AS total_emprestimo
FROM 
  tb_itens_emprestados ie
JOIN 
  tb_livros l ON ie.id_livro = l.id_livro
GROUP BY 
  ie.id_emprestimo
ORDER BY 
  ie.id_emprestimo;
*/