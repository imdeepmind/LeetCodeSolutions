-- Write your PostgreSQL query statement below
SELECT product_id, COALESCE(ROUND(SUM(total_cost) / SUM(units)::decimal, 2), 0) as average_price FROM (
    SELECT P.product_id, US.units, P.price, US.units * P.price AS total_cost FROM Prices P
    LEFT JOIN UnitsSold US
    ON US.product_id = P.product_id AND US.purchase_date BETWEEN P.start_date AND p.end_date
    WHERE P.product_id IS NOT NULL
) as tmp
GROUP BY product_id
-- GROUP BY P.product_id, US.product_id


-- SELECT * FROM (
--     SELECT P.product_id, US.units, P.price, US.units * P.price AS total_cost FROM Prices P
--     LEFT JOIN UnitsSold US
--     ON US.product_id = P.product_id AND US.purchase_date BETWEEN P.start_date AND p.end_date
--     WHERE P.product_id IS NOT NULL
-- ) as tmp
