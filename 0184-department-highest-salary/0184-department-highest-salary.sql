-- Write your PostgreSQL query statement below
SELECT D.name as Department, tmp.name AS Employee, tmp.salary as Salary FROM (
    SELECT
        *,
        RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) as sal_rank 
    FROM Employee
) AS tmp
INNER JOIN Department D
    ON D.id = tmp.departmentId
WHERE tmp.sal_rank = 1