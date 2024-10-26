-- Write your PostgreSQL query statement below
SELECT
    user_id as buyer_id,
    join_date,
    (
        SELECT COUNT(*)
        FROM Orders
        WHERE EXTRACT(YEAR FROM order_date) = 2019 AND buyer_id = user_id
    ) AS orders_in_2019
FROM Users