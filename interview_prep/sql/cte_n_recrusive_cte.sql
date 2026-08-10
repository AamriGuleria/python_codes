-- Write a CTE that computes department average salary, then joins it back to employees to flag who earns above their department's average.

WITH Avg_Salary AS (
    SELECT d.dept_id, d.dept_name, AVG(e.salary) as avg_salary 
    FROM departments d 
    JOIN employees e ON d.dept_id = e.dept_id 
    GROUP BY d.dept_id, d.dept_name
) 
SELECT e.emp_id, e.emp_name, a.avg_salary 
FROM employees e 
JOIN Avg_Salary a ON e.dept_id = a.dept_id;
-- ALTERNATIVE
SELECT 
    e.emp_id, 
    e.emp_name, 
    AVG(e.salary) OVER (PARTITION BY e.dept_id) AS avg_salary
FROM employees e;