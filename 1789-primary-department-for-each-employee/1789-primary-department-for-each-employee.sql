-- Write your PostgreSQL query statement below
SELECT 
    E.employee_id,
    E.department_id
FROM (
    SELECT 
        *,
        COUNT(employee_id) OVER(partition by employee_id) as no_of_dept
    FROM Employee
) E
WHERE 
    E.no_of_dept = 1 OR E.primary_flag = 'Y'