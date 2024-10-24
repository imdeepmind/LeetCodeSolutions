-- Write your PostgreSQL query statement below
-- SELECT * FROM (
--     SELECT SecondHighestSalary FROM (
--         SELECT 
--             salary as SecondHighestSalary
--             ,DENSE_RANK() OVER(ORDER BY salary DESC) as salary_rank
--         FROM Employee
--     ) tmp
--     WHERE tmp.salary_rank = 2
--     UNION 
--     SELECT NULL AS SecondHighestSalary
-- )
-- ORDER BY SecondHighestSalary 
-- LIMIT 1

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary != (SELECT MAX(salary) FROM Employee)