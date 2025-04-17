-- Write your PostgreSQL query statement below
SELECT
    P.product_name,
    S.year,
    S.price
FROM Sales S
LEFT JOIN Product P
on P.product_id = S.product_id