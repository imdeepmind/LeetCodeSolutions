-- Write your PostgreSQL query statement below
UPDATE Salary S
SET sex = CASE WHEN S.sex = 'f' THEN 'm' ELSE 'f' END