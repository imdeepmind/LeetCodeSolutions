-- Write your PostgreSQL query statement below
WITH tmp_table AS (
    SELECT 
        user_id,
        ROUND((
            SELECT COUNT(*) 
            FROM Confirmations C 
            WHERE 
                C.action = 'confirmed' AND 
                C.user_id = OC.user_id
            ) / (
                SELECT COUNT(*)::decimal
                FROM Confirmations C 
                WHERE 
                    C.user_id = OC.user_id
            ) 
        ,2) AS confirmation_rate
    FROM Confirmations OC
    GROUP BY user_id
)
SELECT 
    S.user_id,
    COALESCE(T.confirmation_rate, 0) AS confirmation_rate
FROM Signups S
LEFT JOIN tmp_table T
    ON T.user_id = S.user_id