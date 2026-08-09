SELECT DISTINCT dept_id
FROM employees;


SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id
HAVING COUNT(emp_id) > 2;



SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;


SELECT dept_id,
       SUM(salary) AS total_salary
FROM employees
GROUP BY dept_id
ORDER BY total_salary DESC;


SELECT *
FROM employees
WHERE hire_date >= '2021-01-01'
ORDER BY hire_date ASC;



SELECT emp_id,
       emp_name,
       dept_id,
       manager_id,
       salary,
       hire_date,
       CASE
           WHEN salary > 85000 THEN 'Senior'
           WHEN salary BETWEEN 70000 AND 85000 THEN 'Mid'
           ELSE 'JUNIOR'
       END AS salary_category
FROM employees;


SELECT emp_id,
       emp_name,
       CASE
           WHEN manager_id IS NOT NULL THEN 'Has Manager'
           ELSE 'No Manager'
       END AS manager_status
FROM employees;



