-- Write your PostgreSQL query statement below
-- SELECT machine_id, AVG(diff) as processing_time FROM (
--     SELECT *, (timestamp - LAG(timestamp) OVER (ORDER BY machine_id)) as diff FROM Activity ORDER BY machine_id
-- )
-- WHERE activity_type = 'end'
-- GROUP BY machine_id

SELECT A1.machine_id, ROUND(AVG(A1.timestamp - A2.timestamp)::decimal, 3) AS processing_time
FROM Activity A1
INNER JOIN Activity A2
    ON A1.machine_id = A2.machine_id AND A1.process_id = A2.process_id AND A2.activity_type = 'start'
WHERE A1.activity_type = 'end'
GROUP BY A1.machine_id