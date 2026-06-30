
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


-- Correlated query
SELECT e.id, e.salary, e.dept
FROM employees e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE dept = e.dept 
);

-- window function approach
WITH employee_stats(id,name,salary,avg_salary)
AS(
select employees.id, employees.name,employees.salary,
AVG(employees.salary) OVER (PARTITION BY employees.dept as avg_salary)
from employees)

SELECT id, salary, dept, avg_salary
FROM employee_stats
WHERE salary > avg_salary;