SELECT
    name,
    salary,
    ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_num
FROM employee;