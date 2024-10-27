-- -- Write your PostgreSQL query statement below
WITH tmp_table AS (
    SELECT transaction_date, SUM(amount) AS amount, amount % 2 = 0 AS is_even
    FROM transactions
    GROUP BY amount % 2 = 0, transaction_date
    ORDER BY transaction_date ASC
)
SELECT 
    transaction_date,
    SUM(odd_sum) AS odd_sum,
    SUM(even_sum) AS even_sum
FROM (
    SELECT 
        transaction_date,
        CASE 
            WHEN is_even = FALSE THEN amount
            ELSE 0
        END AS odd_sum,
        CASE 
            WHEN is_even = TRUE THEN amount
            ELSE 0
        END AS even_sum
    FROM tmp_table
)
GROUP BY transaction_date
