-- Write your PostgreSQL query statement below
SELECT * FROM (
    SELECT 
    E1.employee_id, 
    name, 
    (SELECT COUNT(E2.reports_to) FROM Employees E2 WHERE reports_to = E1.employee_id) AS reports_count,
    ROUND((SELECT AVG(E2.age) FROM Employees E2 WHERE reports_to = E1.employee_id)) as average_age
    FROM Employees E1
)
WHERE reports_count > 0
ORDER BY employee_id