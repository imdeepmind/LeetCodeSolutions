-- Write your PostgreSQL query statement below
SELECT
    A.player_id,
    MIN(A.event_date) as first_login
FROM Activity A
GROUP BY A.player_id
