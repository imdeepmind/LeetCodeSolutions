-- Write your PostgreSQL query statement below
SELECT coalesce(E.employee_id, S.employee_id) AS employee_id
FROM Employees E
FULL OUTER JOIN Salaries S
    ON S.employee_id = E.employee_id
WHERE E.name IS NULL OR S.salary IS NULL
ORDER BY coalesce(E.employee_id, S.employee_id)