-- Write your PostgreSQL query statement below
SELECT
    AD.actor_id,
    AD.director_id
FROM ActorDirector AD
GROUP BY AD.actor_id, AD.director_id
HAVING COUNT(*) > 2