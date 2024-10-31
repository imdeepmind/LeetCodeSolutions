-- Write your PostgreSQL query statement below
SELECT 
    T.request_at AS "Day",
    ROUND(COUNT(*) FILTER(WHERE T.status != 'completed') / COUNT(*)::decimal, 2) AS "Cancellation Rate"
FROM Trips T
INNER JOIN Users U
    ON U.users_id = T.client_id
INNER JOIN Users D
    ON D.users_id = T.driver_id
WHERE U.banned = 'No' AND D.banned = 'No' AND T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.request_at
