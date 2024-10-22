-- Write your PostgreSQL query statement below
SELECT P.product_name, O.unit FROM (
    SELECT O.product_id, SUM(O.unit) AS unit FROM Orders O
    WHERE 
        EXTRACT(YEAR FROM O.order_date) = 2020 AND EXTRACT(MONTH FROM O.order_date) = 2
    GROUP BY O.product_id
    HAVING SUM(O.unit) > 99
) O
INNER JOIN Products P
ON O.product_id = P.product_id