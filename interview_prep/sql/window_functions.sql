-- 1. RANK() within each department
SELECT e.emp_id,
       e.emp_name,
       d.dept_id,
       RANK() OVER (
           PARTITION BY d.dept_id
           ORDER BY e.salary DESC
       )
FROM employees e
JOIN departments d
  ON e.dept_id = d.dept_id;



-- 2 Same using DENSE_RANK()
SELECT e.emp_id,
       e.emp_name,
       d.dept_id,
       DENSE_RANK() OVER (
           PARTITION BY d.dept_id
           ORDER BY e.salary DESC
       )
FROM employees e
JOIN departments d
  ON e.dept_id = d.dept_id;



-- 3 Highest Paid Employee Within Each department
WITH RANKED_EMPLOYEES AS (
    SELECT e.emp_id,
           e.emp_name,
           d.dept_id,
           ROW_NUMBER() OVER (
               PARTITION BY d.dept_id
               ORDER BY e.salary DESC
           ) AS rn
    FROM employees e
    JOIN departments d
      ON e.dept_id = d.dept_id
)
SELECT *
FROM RANKED_EMPLOYEES
WHERE rn = 1;


-- 4. Previous hire using LAG()
SELECT e.emp_id,
       e.emp_name,
       d.dept_id,
       e.hire_date,
       LAG(e.hire_date) OVER (
           PARTITION BY d.dept_id
           ORDER BY e.hire_date
       ) AS prev_hire_date
FROM employees e
JOIN departments d
  ON e.dept_id = d.dept_id;


-- 5. Next-hired employee's salary using LEAD()
SELECT e.emp_id,
       e.emp_name,
       d.dept_id,
       e.hire_date,
       e.salary,
       LEAD(e.salary) OVER (
           PARTITION BY d.dept_id
           ORDER BY e.hire_date
       ) AS next_salary
FROM employees e
JOIN departments d
  ON e.dept_id = d.dept_id;