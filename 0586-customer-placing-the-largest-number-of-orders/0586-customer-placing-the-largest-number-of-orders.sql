-- Write your PostgreSQL query statement below
SELECT 
    O.customer_number
FROM Orders O
GROUP BY O.customer_number
ORDER BY COUNT(O.order_number) DESC
LIMIT 1