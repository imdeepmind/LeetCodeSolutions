-- Write your PostgreSQL query statement below
(
    SELECT 
        MN.num
    FROM MyNumbers MN
    GROUP BY MN.num
    HAVING COUNT(MN.num) <= 1
    ORDER BY MN.num DESC
)
UNION ALL
(SELECT NULL as "num")
LIMIT 1