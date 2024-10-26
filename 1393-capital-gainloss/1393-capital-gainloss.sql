-- Write your PostgreSQL query statement below
-- WITH tmp_table AS (
--     SELECT 
--         *,
--         LEAD(price) OVER(ORDER BY stock_name, operation_day) AS sell_price
--     FROM Stocks
--     ORDER BY stock_name, operation_day
-- )
-- SELECT 
--     stock_name,
--     SUM(sell_price - price) AS capital_gain_loss
-- FROM tmp_table
-- WHERE operation = 'Buy'
-- GROUP BY stock_name

-- 1000


SELECT 
    sell.stock_name,
    sell.price - buy.price AS capital_gain_loss
FROM (
    SELECT 
        stock_name, 
        SUM(price) AS price 
    FROM Stocks
    WHERE operation = 'Buy'
    GROUP BY stock_name
) buy
INNER JOIN (
    SELECT 
        stock_name, 
        SUM(price) AS price 
    FROM Stocks
    WHERE operation = 'Sell'
    GROUP BY stock_name
) sell
    ON sell.stock_name = buy.stock_name
