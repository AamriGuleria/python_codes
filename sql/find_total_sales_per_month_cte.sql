


WITH sales_stats(month, monthly_sale_amount)
AS(
  SELECT FORMAT(sale_date,'yyyy-MM'),SUM(amount)
  FROM sales
  GROUP BY FORMAT(sale_date, 'yyyy-MM')
)

SELECT * FROM sales_stats
ORDER BY month;