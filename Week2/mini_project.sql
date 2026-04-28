Select c.name, count(o.order_id) AS total_orders,
COALESCE(SUM(o.amount), 0) AS total_revenue

FROM customers c 
Left JOIN orders o /* using left join retrives all the values on customers table not only the common value*/
ON c.id = o.customer_id
Group by c.name;
