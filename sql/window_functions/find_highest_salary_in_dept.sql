


SELECT dept, MAX(salary)
FROM employees
GROUP BY dept


SELECT 
    employee, 
    dept, 
    salary, 
    MAX(salary) OVER (PARTITION BY dept) AS max_dept_salary
FROM employees;