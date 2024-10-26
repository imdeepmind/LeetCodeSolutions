-- Write your PostgreSQL query statement below
SELECT 
    DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        id,
        num,
        LEAD(num, 1) OVER() as next_num,
        LEAD(num, 2) OVER() as next_next_num
    FROM Logs
)
WHERE num = next_num AND next_num = next_next_num