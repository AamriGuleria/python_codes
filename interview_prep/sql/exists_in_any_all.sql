SELECT *
FROM employees
WHERE dept_id IN (
    SELECT dept_id
    FROM departments
    WHERE dept_name = 'Engineering'
);



SELECT *
FROM employees e
WHERE EXISTS (
    SELECT 1
    FROM departments d
    WHERE d.dept_id = e.dept_id
      AND d.dept_name = 'Engineering'
);



SELECT *
FROM employees
WHERE salary > ANY (
    SELECT salary
    FROM employees
    WHERE dept_id IN (
        SELECT dept_id
        FROM departments
        WHERE dept_name = 'HR'
    )
);




SELECT *
FROM employees
WHERE salary > ALL (
    SELECT salary
    FROM employees
    WHERE dept_id IN (
        SELECT dept_id
        FROM departments
        WHERE dept_name = 'HR'
    )
);



SELECT d.*
FROM departments d
WHERE NOT EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.dept_id = d.dept_id
);