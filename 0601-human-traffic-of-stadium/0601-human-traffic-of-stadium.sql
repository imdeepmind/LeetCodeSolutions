-- -- Write your PostgreSQL query statement below
WITH tmp_table AS (
    SELECT 
        *
    FROM (
        SELECT 
            id,
            LEAD(id, 1) OVER() AS next_id,
            LEAD(id, 2) OVER() AS next_next_id
        FROM Stadium
        WHERE people >= 100
    )
    WHERE (id + 1 = next_id and next_id + 1 = next_next_id)
)
SELECT * FROM Stadium 
WHERE id IN (
    SELECT id FROM tmp_table
    UNION SELECT next_id AS id FROM tmp_table
    UNION SELECT next_next_id AS id FROM tmp_table
)
ORDER BY visit_date ASC
