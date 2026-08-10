SELECT e.emp_id, e.emp_name, d.dept_name
FROM employees e
JOIN departments d
  ON d.dept_id = e.dept_id;


SELECT e.*, d.dept_id
FROM employees e
LEFT JOIN departments d
  ON d.dept_id = e.dept_id;



SELECT d.*, COUNT(e.emp_id)
FROM departments d
LEFT JOIN employees e
  ON d.dept_id = e.dept_id
GROUP BY d.dept_id;


SELECT d.*, e.*
FROM departments d
FULL OUTER JOIN employees e
  ON d.dept_id = e.dept_id;


SELECT e.emp_id,
       e.emp_name,
       m.emp_name AS manager_name
FROM employees e
LEFT JOIN employees m
  ON e.manager_id = m.emp_id;




SELECT e.*, d.*
FROM employees e
CROSS JOIN departments d;


