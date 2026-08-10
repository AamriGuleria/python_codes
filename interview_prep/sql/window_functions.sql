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


-- Use FIRST_VALUE() to show the name of the earliest-hired employee in each department, next to every row in that department
-- Use LAST_VALUE() to show the most recent hire in each department next to every row — and explain why you need to adjust the frame (ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) to get a correct answer.

SELECT 
    d.dept_id, 
    d.dept_name, 
    e.emp_name,
    -- Earliest hired name
    FIRST_VALUE(e.emp_name) OVER (
        PARTITION BY d.dept_id 
        ORDER BY e.hire_date ASC
    ) AS earliest_hire_name,
    
    -- Most recent hired name
    LAST_VALUE(e.emp_name) OVER (
        PARTITION BY d.dept_id 
        ORDER BY e.hire_date ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS latest_hire_name
FROM 
    departments d 
JOIN 
    employees e ON d.dept_id = e.dept_id;   
