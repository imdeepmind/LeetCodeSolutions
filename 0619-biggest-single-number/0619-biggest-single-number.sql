-- Write your PostgreSQL query statement below
(
    SELECT num FROM MyNumbers
    GROUP BY num
    HAVING count(num) = 1
    ORDER BY num DESC
    LIMIT 1
) 
UNION (SELECT null as num)
LIMIT 1