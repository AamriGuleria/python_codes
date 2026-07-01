
-- My Solution using nested query
SELECT customer_id, first_name, last_name, age, country
FROM customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id FROM orders
);


-- Exists/Not Exists approach
SELECT customer_id, first_name, last_name, age, country
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
)