-- Write your PostgreSQL query statement below
SELECT 
    W2.id
FROM Weather W1
LEFT JOIN Weather W2
ON W2.recordDate = DATE(W1.recordDate) + 1
WHERE W2.temperature > W1.temperature