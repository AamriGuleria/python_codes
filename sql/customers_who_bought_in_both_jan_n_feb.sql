

SELECT 
  customer_id,
  customer_name
FROM purchases
WHERE FORMAT(purchase_date, 'yyyy-MM') IN ('2026-01', '2026-02')
GROUP BY customer_id, customer_name
HAVING COUNT(DISTINCT FORMAT(purchase_date, 'yyyy-MM')) = 2;