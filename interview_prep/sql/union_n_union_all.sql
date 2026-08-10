-- Combine a list of "high earners" (salary > 90000) and "long tenured" (hired before 2019) employees into one result set with UNION (no duplicates).
-- Do the same with UNION ALL and explain in a comment what's different about the row count if an employee qualifies for both.



SELECT * 
FROM employees 
WHERE salary > 90000

UNION

SELECT * 
FROM employees 
WHERE hire_date < '2019-01-01';


SELECT * 
FROM employees 
WHERE salary > 90000

UNION ALL

SELECT * 
FROM employees 
WHERE hire_date < '2019-01-01';   