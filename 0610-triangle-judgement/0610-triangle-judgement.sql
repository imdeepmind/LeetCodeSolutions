-- Write your PostgreSQL query statement below
SELECT
    T.x,
    T.y,
    T.z,
    CASE 
        WHEN T.x+T.y > T.z AND T.y + T.z > T.x AND T.x + T.z > T.y 
            THEN 'Yes'
            ELSE 'No' 
        END AS "triangle"
FROM Triangle T