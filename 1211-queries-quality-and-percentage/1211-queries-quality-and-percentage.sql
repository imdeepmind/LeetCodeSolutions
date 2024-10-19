-- Write your PostgreSQL query statement below
SELECT 
    query_name,
    ROUND(AVG(rating / position::decimal), 2) as quality,
    ROUND(SUM((rating < 3)::int) * 100. / COUNT(*), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name