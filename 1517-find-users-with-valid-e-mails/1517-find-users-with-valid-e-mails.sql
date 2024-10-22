-- Write your PostgreSQL query statement below
SELECT * FROM Users U
WHERE 
    U.mail ~ '^[A-Za-z0-9_.-]+@leetcode\.com$'
    AND regexp_like(SUBSTRING(U.mail, 1, 1),'[a-zA-Z]') 
