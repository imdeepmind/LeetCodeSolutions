-- Write your PostgreSQL query statement below
-- SELECT 
--     E.name
-- FROM Employee E
-- WHERE (
--     SELECT COUNT(*) FROM Employee E2 WHERE E2.managerId = E.id
-- ) >= 5

WITH tmp_table AS (
    SELECT managerId
    FROM Employee 
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
)
SELECT name
FROM Employee E
WHERE E.id IN (SELECT DISTINCT managerId FROM tmp_table)