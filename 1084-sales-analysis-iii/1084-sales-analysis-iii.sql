-- Write your PostgreSQL query statement below
SELECT
    S.product_id,
    P.product_name
FROM Product P
INNER JOIN Sales S
ON S.product_id = P.product_id
GROUP BY S.product_id, P.product_name
HAVING MIN(S.sale_date) >= '2019-01-01' AND MAX(S.sale_date) <= '2019-03-31'
