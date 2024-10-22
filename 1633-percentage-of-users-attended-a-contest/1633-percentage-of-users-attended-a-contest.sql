-- Write your PostgreSQL query statement below
SELECT R.contest_id, ROUND((COUNT(R.user_id) / (SELECT COUNT(DISTINCT user_id)::decimal FROM Users)) * 100, 2) AS percentage
FROM Register R
GROUP BY R.contest_id
ORDER BY ROUND((COUNT(R.user_id) / (SELECT COUNT(DISTINCT user_id)::decimal FROM Users)) * 100, 2) DESC, R.contest_id ASC