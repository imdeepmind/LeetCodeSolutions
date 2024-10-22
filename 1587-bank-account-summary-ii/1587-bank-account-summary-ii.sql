-- Write your PostgreSQL query statement below
SELECT U.name, T.balance
FROM (
    SELECT T.account, SUM(T.amount) as balance
    FROM Transactions T
    GROUP BY T.account
    HAVING SUM(T.amount) > 10000
) T
INNER JOIN Users U
ON U.account = T.account