-- Write your PostgreSQL query statement below
SELECT 
    id,
    SUM(num) AS num
FROM (
    SELECT 
        requester_id AS id,
        COUNT(requester_id) AS num
    FROM RequestAccepted
    GROUP BY requester_id
    UNION ALL
    SELECT 
        accepter_id AS id,
        COUNT(accepter_id) AS num
    FROM RequestAccepted
    GROUP BY accepter_id
)
GROUP BY id
ORDER BY SUM(num) DESC
LIMIT 1
