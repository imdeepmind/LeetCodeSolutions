CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT 
        CASE 
            WHEN N > 0 THEN (
                SELECT DISTINCT E.salary
                FROM Employee E
                ORDER BY E.salary DESC
                LIMIT 1
                OFFSET N-1
            )
            ELSE (
                null::INT
            )
        END
  );
END;
$$ LANGUAGE plpgsql;

