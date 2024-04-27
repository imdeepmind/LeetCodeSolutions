-- Write your PostgreSQL query statement below
SELECT e.name as employee FROM employee e
LEFT JOIN employee m
ON m.id = e.managerId
WHERE e.salary > m.salary