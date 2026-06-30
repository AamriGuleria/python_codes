
-- My Solution with cte
WITH Avg_Salary(average_salary, dept) AS (
    SELECT AVG(salary) as average_salary, dept
    FROM employees
    GROUP BY dept
)
SELECT e.id, e.salary, e.dept, Avg_Salary.average_salary
FROM employees e
JOIN Avg_Salary
    ON e.dept = Avg_Salary.dept
WHERE e.salary > Avg_Salary.average_salary;