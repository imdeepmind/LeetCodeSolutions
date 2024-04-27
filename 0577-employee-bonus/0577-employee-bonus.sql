-- Write your PostgreSQL query statement below
SELECT e.name, b.bonus
FROM employee e
LEFT JOIN bonus b
ON e.empId = b.empId
WHERE b.bonus < 1000 or b.bonus IS NULL
