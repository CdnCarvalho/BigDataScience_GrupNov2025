SELECT *
FROM Vendas;

SELECT Produto, QuantidadeVendida
 FROM vendas;
 
SELECT Produto, Valor
FROM Vendas
WHERE Valor > 100;

SELECT DataVenda, Produto, Valor
FROM Vendas
WHERE DataVenda >= '2024-05-01';

SELECT Produto, Loja
FROM vendas 
WHERE QuantidadeVendida > 20;

SELECT Produto, Valor, QuantidadeVendida
FROM vendas 
WHERE Loja = 'Niterói' AND DataVenda < '2024-01-01';

SELECT Produto, Valor, DataVenda
FROM Vendas 
WHERE DataVenda >= '2024-07-01' AND DataVenda <= '2024-09-30';

SELECT Produto, Valor, DataVenda
FROM vendas
WHERE DataVenda BETWEEN "2024-07-01" AND "2024-09-30";

SELECT Produto, Valor, QuantidadeVendida, DataVenda
FROM Vendas
WHERE DataVenda BETWEEN '2024-09-15' AND '2024-10-20' 
AND Categoria = 'Eletrônicos';

SELECT * 
FROM importacao 
LIMIT 10;
