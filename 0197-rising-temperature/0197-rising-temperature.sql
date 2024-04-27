-- Write your PostgreSQL query statement below
SELECT w2.id FROM weather w1
LEFT JOIN weather w2
ON DATE(w1.recordDate) + 1 = w2.recordDate
WHERE w2.temperature > w1.temperature