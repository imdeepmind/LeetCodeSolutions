-- Write your PostgreSQL query statement below
SELECT 
    C.name
FROM Customer C
WHERE C.referee_id != 2 OR C.referee_id IS NULL