-- Write your PostgreSQL query statement below
SELECT DISTINCT results FROM (
    (
        SELECT U.name results
        FROM MovieRating MR
        INNER JOIN Users U
            ON U.user_id = MR.user_id
        GROUP BY MR.user_id, U.name
        ORDER BY COUNT(MR.user_id) DESC, name ASC
        LIMIT 1
    )
    UNION
    (
        SELECT
            M.title AS results
        FROM MovieRating MR
        INNER JOIN Movies M
            ON M.movie_id = MR.movie_id
        WHERE EXTRACT(MONTH FROM MR.created_at) = 2 AND EXTRACT(YEAR FROM MR.created_at) = 2020
        GROUP BY MR.movie_id, M.title
        ORDER BY AVG(MR.rating) DESC, M.title
        LIMIT 1
    )
)