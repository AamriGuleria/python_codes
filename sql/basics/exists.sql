
SELECT * FROM customers c where EXISTS(
SELECT 1 FROM orders o WHERE o.cid == c.id and o.status == "shipped"
)