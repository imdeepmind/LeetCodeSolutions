-- Write your PostgreSQL query statement below
DELETE FROM person
    WHERE id NOT IN (
        SELECT MIN(id)
        FROM person
        GROUP BY email
    )
    AND email IN (
        SELECT email
        FROM person
        GROUP BY email
        HAVING COUNT(*) > 1
    );