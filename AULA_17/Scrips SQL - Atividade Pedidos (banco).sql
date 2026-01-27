/* CHAVES DAS ATIVIDADES */
-- CHAVE PRIMÁRIA

-- Tabela clientes
ALTER TABLE clientes
MODIFY COLUMN codigo_cliente INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_cliente);

-- Tabela produtos
ALTER TABLE produtos
MODIFY COLUMN codigo_produto INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_produto);

-- Tabela pedidos
ALTER TABLE tb_pedidos
MODIFY COLUMN codigo_pedido INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_pedido);

-- Tabela itens
ALTER TABLE tb_itens
MODIFY COLUMN codigo_item INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_item);
-- --------------------------------------------------


-- CHAVE ESTRANGEIRA CLIENTE -> PEDIDO
ALTER TABLE tb_pedidos
ADD CONSTRAINT fk_tb_pedidos_clientes
FOREIGN KEY (cliente_codigo)
REFERENCES clientes (codigo_cliente);

-- CHAVE ESTRANGEIRA ITENS -> PEDIDO
ALTER TABLE tb_itens
ADD CONSTRAINT fk_tb_itens_pedidos
FOREIGN KEY (pedido_codigo)
REFERENCES tb_pedidos (codigo_pedido);

-- CHAVE ESTRANGEIRA ITENS -> PRODUTO
ALTER TABLE tb_itens
ADD CONSTRAINT fk_tb_itens_produtos
FOREIGN KEY (codigo_produto)
REFERENCES produtos (codigo_produto);
-- -------------------------------------------


-- Mostre os produtos comprados em cada pedido com suas quantidades.
SELECT tb_pedidos.codigo_pedido, tb_produtos.produto, tb_itens.quantidade
FROM tb_itens
JOIN tb_pedidos ON tb_itens.pedido_codigo = tb_pedidos.codigo_pedido
JOIN tb_produtos ON tb_itens.item_codigo = tb_produtos.codigo_produto;

-- Liste os pedidos feitos por clientes que moram em São Paulo.
SELECT 
tb_clientes.nome, 
tb_clientes.sobrenome, 
tb_pedidos.codigo_pedido, 
tb_pedidos.data_pedido
FROM tb_pedidos
JOIN tb_clientes ON tb_pedidos.cliente_codigo = tb_clientes.cod_cliente
WHERE tb_clientes.cidade = 'São Paulo';