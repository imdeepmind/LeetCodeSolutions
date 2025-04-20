-- Write your PostgreSQL query statement below
SELECT 
    P.product_id,
    ROUND(SUM(P.total_earning) / SUM(P.units)::decimal, 2) AS "average_price"
FROM (
    SELECT
        P.product_id,
        US.units * P.price AS "total_earning",
        US.units
    FROM Prices P
    INNER JOIN UnitsSold US
    ON US.product_id = P.product_id AND US.purchase_date BETWEEN P.start_date AND P.end_date
) as P
GROUP BY P.product_id
