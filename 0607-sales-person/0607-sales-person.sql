-- Write your PostgreSQL query statement below
SELECT DISTINCT SP.name
FROM SalesPerson SP
LEFT JOIN Orders O
ON O.sales_id = SP.sales_id
WHERE O.sales_id NOT IN (SELECT DISTINCT sales_id FROM Orders WHERE com_id IN (SELECT DISTINCT com_id FROM Company WHERE name = 'RED')) OR O.sales_id IS NULL

-- LEFT JOIN (
--     SELECT sales_id
--     FROM Orders O
--     WHERE O.sales_id NOT IN (SELECT DISTINCT sales_id FROM Orders WHERE com_id = 1)
-- ) O