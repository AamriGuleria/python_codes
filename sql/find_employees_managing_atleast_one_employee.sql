

select employee_id,first_name,last_name,manager_id
from employees e
WHERE EXISTS(
  SELECT 1
  from employees f
  where e.employee_id = f.manager_id
)