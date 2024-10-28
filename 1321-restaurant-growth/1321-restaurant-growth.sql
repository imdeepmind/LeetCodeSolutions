-- Write your PostgreSQL query statement below
WITH tmp_table AS (
    SELECT 
        C1.visited_on,
        (
            SELECT 
                SUM(amount) 
            FROM Customer C2 
            WHERE C2.visited_on BETWEEN C1.visited_on - interval '6 days' AND C1.visited_on
        ) AS total,
        (
            SELECT 
                COUNT(amount) 
            FROM Customer C2 
            WHERE C2.visited_on BETWEEN C1.visited_on - interval '6 days' AND C1.visited_on
        ) AS count_total
    FROM Customer C1
)
SELECT 
    visited_on,
    MAX(total) as amount,
    ROUND(MAX(total) / 7::decimal, 2) AS average_amount
FROM tmp_table
WHERE count_total > 6
GROUP BY visited_on
ORDER BY visited_on