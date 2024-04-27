-- Write your PostgreSQL query statement below
SELECT c.name as customers FROM customers c
LEFT JOIN orders o
ON o.customerId = c.id
WHERE o.id IS NULL