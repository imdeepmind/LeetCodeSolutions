-- Write your PostgreSQL query statement below
SELECT 
    id,
    CASE
        WHEN student IS NOT NULL THEN student
        ELSE originalStudent
    END AS student
FROM (
    SELECT 
        id,
        student AS originalStudent,
        CASE 
            WHEN id % 2 != 0 THEN LEAD(student) over(ORDER BY id ASC)
            ELSE LAG(student) over(ORDER BY id ASC)
        END AS student
    FROM Seat
    ORDER BY id ASC
)
