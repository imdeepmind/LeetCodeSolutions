-- Write your PostgreSQL query statement below
-- SELECT S.product_id, P.product_name FROM Sales S
-- INNER JOIN Product P
-- ON P.product_id = S.product_id
-- WHERE EXTRACT(MONTH FROM S.sale_date) < 4 AND EXTRACT(YEAR FROM S.sale_date) = 2019
-- AND S.product_id NOT IN (
--     SELECT S.product_id FROM Sales S
--     WHERE EXTRACT(MONTH FROM S.sale_date) >= 4 AND EXTRACT(YEAR FROM S.sale_date) = 2019
-- )


SELECT S.product_id, P.product_name FROM Sales S
INNER JOIN Product P
ON P.product_id = S.product_id
GROUP BY S.product_id, P.product_name
HAVING MIN(S.sale_date) >= '2019-01-01' AND MAX(S.sale_date) <= '2019-03-31'