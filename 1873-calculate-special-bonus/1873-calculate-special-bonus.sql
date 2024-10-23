-- Write your PostgreSQL query statement below
SELECT 
    employee_id,
    CASE 
        WHEN employee_id % 2 != 0 AND UPPER(SUBSTRING(name, 1, 1)) != 'M' THEN salary
        ELSE 0
    END AS bonus
FROM Employees
ORDER BY employee_id