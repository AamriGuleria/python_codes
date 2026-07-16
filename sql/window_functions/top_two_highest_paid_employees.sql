SELECT *
FROM (
    SELECT
        id, name, department, salary, hire_date,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
    FROM employee
) sub
WHERE rnk IN (1, 2);