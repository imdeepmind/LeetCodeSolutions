-- Write your PostgreSQL query statement below
SELECT  
    person_name
FROM (
    SELECT
        *,
        (SELECT SUM(weight) FROM Queue QI WHERE QI.turn <= Q.turn) AS total_weight
    FROM Queue Q
    ORDER BY Q.turn
)
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1