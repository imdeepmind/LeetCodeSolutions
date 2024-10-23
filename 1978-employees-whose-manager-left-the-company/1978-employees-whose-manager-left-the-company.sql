-- Write your PostgreSQL query statement below
SELECT E1.employee_id
FROM Employees E1
LEFT JOIN Employees E2
    ON E1.manager_id = E2.employee_id
WHERE E1.salary < 30000 AND E1.manager_id IS NOT NULL AND E2.employee_id IS NULL
ORDER BY E1.employee_id