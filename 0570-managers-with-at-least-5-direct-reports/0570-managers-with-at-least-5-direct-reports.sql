-- Write your PostgreSQL query statement below
SELECT 
    E.name
FROM Employee E
WHERE (
    SELECT COUNT(*) FROM Employee E2 WHERE E2.managerId = E.id
) >= 5