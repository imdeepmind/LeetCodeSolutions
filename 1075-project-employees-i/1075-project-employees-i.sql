-- Write your PostgreSQL query statement below
SELECT project_id, ROUND(AVG(e.experience_years), 2) AS average_years FROM Project p
INNER JOIN Employee e
ON e.employee_id = p.employee_id
GROUP BY project_id
