-- Write your PostgreSQL query statement below
SELECT 
    category,
    SUM(accounts_count) AS accounts_count
FROM (
    (SELECT 
        category,
        COUNT(category) AS accounts_count
    FROM (
        SELECT 
            CASE    
                WHEN A.income < 20000 THEN 'Low Salary'
                WHEN A.income BETWEEN 20000 AND 50000 THEN 'Average Salary'
                ELSE 'High Salary'
            END AS category
        FROM Accounts A
    )
    GROUP BY category)
    UNION 
    SELECT 'Low Salary' AS category, 0 AS accounts_count
    UNION
    SELECT 'Average Salary' AS category, 0 AS accounts_count
    UNION
    SELECT 'High Salary' AS category, 0 AS accounts_count
)
GROUP BY category