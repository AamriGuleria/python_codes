WITH RECURSIVE descendants AS (
    SELECT employee_id, name, manager_id, title, 1 AS level
    FROM employees
    WHERE manager_id = 2 

    UNION ALL


    SELECT e.employee_id, e.name, e.manager_id, e.title, d.level + 1
    FROM employees e
    JOIN descendants d ON e.manager_id = d.employee_id
)
SELECT * FROM descendants
ORDER BY level, employee_id;