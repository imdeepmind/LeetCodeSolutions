-- Write your PostgreSQL query statement below
WITH tmp_table AS (
    SELECT 
        *
    FROM (
        SELECT
            *,
            CASE 
                WHEN order_date = customer_pref_delivery_date THEN 'immediate' 
                ELSE 'scheduled'
            END delivery_status,
            RANK() OVER(PARTITION BY customer_id ORDER BY order_date) AS order_rank
        FROM Delivery
    )
    WHERE order_rank = 1
)
SELECT 
    ROUND((((SELECT COUNT(*) FROM tmp_table WHERE delivery_status = 'immediate') / (SELECT COUNT(*)::decimal FROM tmp_table)) * 100), 2)
AS immediate_percentage