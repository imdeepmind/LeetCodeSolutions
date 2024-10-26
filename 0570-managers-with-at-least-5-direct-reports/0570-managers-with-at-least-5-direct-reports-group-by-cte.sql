-- Write your PostgreSQL query statement below
-- SELECT 
--     E.name
-- FROM Employee E
-- WHERE (
--     SELECT COUNT(*) FROM Employee E2 WHERE E2.managerId = E.id
-- ) >= 5

WITH tmp_table AS (
    SELECT managerId, COUNT(*) AS total
    FROM Employee 
    GROUP BY managerId
)
SELECT 
    E.name
FROM tmp_table T
INNER JOIN Employee E
    ON E.id = T.managerId
WHERE total >= 5