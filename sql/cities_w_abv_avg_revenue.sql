

SELECT city, revenue, average_revenue
FROM (
    SELECT city,
           revenue,
           AVG(revenue) OVER () AS average_revenue
    FROM city_revenue
) t
WHERE revenue > average_revenue;