


SELECT dept, MAX(salary)
FROM employees
GROUP BY dept


SELECT employee, dept , salary , MAX(salary) OVER(dept) from employeesis this correct for highest salary in dept??Thought for 2sThought for 2sNot quite — the syntax is wrong. OVER() needs a PARTITION BY clause, you can't just put the column name directly inside the parentheses.
Here's the corrected version:
sqlSELECT 
    employee, 
    dept, 
    salary, 
    MAX(salary) OVER (PARTITION BY dept) AS max_dept_salary
FROM employees;