-- Write your PostgreSQL query statement below
SELECT  
    person_name
FROM (
    SELECT
        *,
        SUM(weight) OVER(ORDER BY turn asc) AS total_weight
    FROM Queue Q
    ORDER BY Q.turn
)
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1