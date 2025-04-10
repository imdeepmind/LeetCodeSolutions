-- Write your PostgreSQL query statement below
SELECT 
    P.email as Email
FROM Person P
GROUP BY P.email
HAVING count(P.email) > 1