CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT * 
    FROM (
        SELECT tmp.salary
        FROM (
            SELECT RANK() OVER(ORDER BY E.salary DESC) AS salary_rank, E.salary
            FROM (
                SELECT DISTINCT EE.salary 
                FROM Employee EE
            ) E
        ) tmp
        WHERE tmp.salary_rank = N
        UNION
        SELECT NULL AS salary
    ) AS ranked_salaries
    ORDER BY salary
    LIMIT 1
  );
END;
$$ LANGUAGE plpgsql;

