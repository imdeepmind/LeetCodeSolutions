-- Write your PostgreSQL query statement below
WITH tmp_table AS (
    SELECT 
        *,
        RANK() OVER(PARTITION BY S.product_id ORDER BY S.year) AS year_rank
    FROM Sales S
)
SELECT 
    T.product_id,
    T.year AS first_year,
    T.quantity,
    T.price
FROM tmp_table T
WHERE T.year_rank = 1
