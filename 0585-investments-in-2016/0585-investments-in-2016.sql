-- Write your PostgreSQL query statement below
WITH CTE1 AS 
        (SELECT 
        pid,tiv_2015, tiv_2016, lat, lon, COUNT(*) OVER(PARTITION BY lat,lon) AS cn
        FROM Insurance),

    CTE2 AS
        (SELECT pid,tiv_2015,tiv_2016,cn, COUNT(*) OVER(pARTITION BY tiv_2015) As ck
        FROM CTE1 
        )

SELECT  
ROUND(SUM(tiv_2016 :: NUMERIC),2) As tiv_2016
FROm CTE2
WHERE cn =1 AND ck >1
