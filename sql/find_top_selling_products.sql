


WITH products_stats(product_id, composite_quantity) AS (
    SELECT product_id, SUM(quantity) AS composite_quantity
    FROM order_items
    GROUP BY product_id
)
SELECT * FROM products_stats
ORDER BY composite_quantity DESC
LIMIT 5;