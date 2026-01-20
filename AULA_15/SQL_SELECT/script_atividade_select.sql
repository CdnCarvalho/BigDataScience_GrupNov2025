
/* ATIVIDADE CONSULTA SQL */

SELECT * FROM importados;

SELECT Pais, Produto, Valor
FROM importados;

SELECT Transacao_ID, Produto, Valor
FROM importados
WHERE Valor > 8000;

SELECT *
FROM importados
WHERE Data >= '2023-01-01';

SELECT Produto, Categoria, Quantidade
FROM importados
WHERE Quantidade > 7000;

SELECT Pais, Produto, Metodo_Envio, Data
FROM importados
WHERE Metodo_Envio = 'Sea'
AND Data < '2022-01-01';

SELECT *
FROM importados
WHERE Data BETWEEN '2022-03-01' AND '2022-06-30';

SELECT Produto, Valor, Categoria, Data
FROM importados
WHERE Categoria = 'Electronics'
AND Data BETWEEN '2023-01-01' AND '2023-12-31';

SELECT Produto, Peso, Pais
FROM importados
WHERE Peso > 4000;


/* Desafio */
SELECT *
FROM importados
WHERE Categoria = 'Electronics'
  AND Metodo_Envio = 'Air'
  AND Quantidade > 2000
  AND Data BETWEEN '2023-01-01' AND '2023-12-31';
  
  
/*------------------------------------------------------*/  
/* AGREGAÇÃO */
SELECT Pais, SUM(Quantidade) AS Total_Quantidade
FROM importados
GROUP BY Pais;

SELECT Pais, SUM(Quantidade) AS Total_Quantidade, ROUND(AVG(Valor),2) AS Valor_Medio
FROM importados
GROUP BY Pais
ORDER BY Total_Quantidade DESC;


/*-------------------------------------------------------*/
/* ALTERAR O TIPO DE DADOS */
ALTER TABLE bd_exemplo_aula_01.importados
MODIFY COLUMN `Data` DATE NULL DEFAULT NULL;
