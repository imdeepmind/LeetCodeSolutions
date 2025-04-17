-- Write your PostgreSQL query statement below
DELETE FROM Person P
WHERE P.email IN (
    SELECT P.email FROM Person P GROUP BY P.email HAVING COUNT(P.*) > 1
) AND P.id NOT IN (
    SELECT MIN(p.id) FROM Person P GROUP BY P.email HAVING COUNT(P.*) > 1
)
