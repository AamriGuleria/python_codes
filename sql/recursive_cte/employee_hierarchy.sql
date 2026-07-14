WITH RECURSIVE employee_hierarchy AS (
    SELECT 
        employee_id, 
        name, 
        manager_id, 
        title, 
        1 AS level
    FROM employees 
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id, 
        e.name, 
        e.manager_id, 
        e.title, 
        eh.level + 1 AS level
    FROM employees e
    JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM employee_hierarchy ORDER BY level, employee_id;