-- -- Write your PostgreSQL query statement below
-- WITH tmp_table AS (
--     SELECT 
--         *,
--         (
--             SELECT 1 
--             FROM Activity A2 
--             WHERE 
--             A1.event_date + interval '1 day' = A2.event_date AND 
--             A2.player_id = A1.player_id
--         ) AS logged_next_day 
--     FROM Activity A1
-- )
-- SELECT (
--     SELECT COUNT(DISTINCT player_id) FROM tmp_table WHERE logged_next_day = 1
-- ), (
--     SELECT COUNT(DISTINCT player_id)::decimal FROM tmp_table
-- ) AS fraction


-- WITH tmp_table AS (
--     SELECT 
--         *,
--         RANK() OVER(partition by player_id ORDER BY event_date ASC) as rank
--     FROM Activity
--     ORDER BY event_date
-- )
-- SELECT ROUND((COUNT(DISTINCT t1.player_id) / (SELECT COUNT(DISTINCT player_id )::decimal FROM Activity)), 2) AS fraction FROM tmp_table t1
-- INNER JOIN tmp_table t2
--     ON t2.rank = 2 AND t1.event_date + interval '1 day' = t2.event_date
-- WHERE t1.rank = 1

WITH tmp_table AS (
    SELECT MIN(event_date) + INTERVAL '1 day' AS next_day, player_id FROM Activity
    GROUP BY player_id
)
SELECT 
    ROUND(COUNT(DISTINCT A1.player_id) / (SELECT COUNT(DISTINCT A2.player_id)::decimal FROM Activity A2), 2) AS fraction
FROM Activity A1
INNER JOIN tmp_table T
    ON T.player_id = A1.player_id AND T.next_day = A1.event_date

-- AND event_date IN (SELECT next_day FROM tmp_table )

-- | next_day            | player_id |
-- | ------------------- | --------- |
-- | 2016-03-03 00:00:00 | 3         |
-- | 2017-06-26 00:00:00 | 2         |
-- | 2016-03-02 00:00:00 | 1         |


-- SELECT MIN(event_date) + INTERVAL '1 day' AS next_day, player_id FROM Activity
--     GROUP BY player_id