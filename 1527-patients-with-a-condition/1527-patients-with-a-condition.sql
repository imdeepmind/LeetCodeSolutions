-- Write your PostgreSQL query statement below
SELECT * 
FROM Patients P
WHERE P.conditions LIKE '% DIAB1%' OR SUBSTRING(P.conditions, 1, 5) = 'DIAB1'