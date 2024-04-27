-- Write your PostgreSQL query statement below
SELECT email FROM (
    SELECT COUNT(*) as total, email FROM person p
    GROUP BY p.email
) as tmp
WHERE tmp.total > 1
