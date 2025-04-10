-- Write your PostgreSQL query statement below
SELECT
    firstName,
    lastName,
    city,
    state
FROM Person P
LEFT JOIN Address A
ON A.personId = P.personId
