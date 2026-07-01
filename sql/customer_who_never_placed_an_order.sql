
-- My Solution using nested query
SELECT customer_id, first_name, last_name, age, country
FROM customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id FROM orders
);