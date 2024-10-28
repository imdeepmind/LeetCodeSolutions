-- Write your PostgreSQL query statement below
WITH temp_tble AS (
    SELECT 
        *,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee
)
SELECT 
    D.name AS Department,
    T.name AS Employee,
    T.Salary
FROM temp_tble T
INNER JOIN Department D
    ON D.id = T.departmentId
WHERE salary_rank < 4