


-- SELECT 
--   sale_month,
--   total_sales AS current_month_sales,
--   LAG(total_sales) OVER (ORDER BY sale_month) AS previous_month_sales,
--   total_sales - LAG(total_sales) OVER (ORDER BY sale_month) AS difference
-- FROM sales;





-- Multi CTE
WITH monthly_sales AS (
  SELECT 
    FORMAT('yyyy-MM', sale_date) AS month,
    SUM(total_sales) AS sales
  FROM sales
  GROUP BY FORMAT('yyyy-MM', sale_date)
),
sales_data AS (
  SELECT
    month,
    sales AS current_month_sale,
    LAG(sales) OVER (ORDER BY month) AS previous_month_sale,
    sales - LAG(sales) OVER (ORDER BY month) AS difference
  FROM monthly_sales
)
SELECT * FROM sales_data;