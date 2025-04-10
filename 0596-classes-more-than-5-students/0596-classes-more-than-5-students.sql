-- Write your PostgreSQL query statement below
SELECT 
    C.class
FROM Courses C
GROUP BY C.class
HAVING COUNT(*) >= 5