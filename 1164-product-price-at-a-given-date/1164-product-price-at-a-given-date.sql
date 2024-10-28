-- Write your PostgreSQL query statement below
-- WITH tmp_table AS (
--     SELECT DISTINCT product_id FROM Products
-- )
-- SELECT
--     T.product_id, COALESCE(MAX(P.new_price), MAX(P2.new_price), 10) AS price
-- FROM tmp_table T
-- LEFT JOIN Products P
--     ON P.product_id = T.product_id AND (
--         P.change_date = '2019-08-16'
--     )
-- LEFT JOIN Products P2
--     ON P2.product_id = T.product_id AND (
--         P2.change_date < '2019-08-16'
--     )
-- GROUP BY T.product_id

SELECT 
    product_id,
    COALESCE(
        (SELECT new_price 
        FROM Products P 
        WHERE 
            P.change_date <= '2019-08-16' AND 
            P.product_id = OP.product_id
        ORDER BY P.change_date DESC 
        LIMIT 1), 10
    ) AS price
FROM (
    SELECT DISTINCT product_id FROM Products 
) OP
