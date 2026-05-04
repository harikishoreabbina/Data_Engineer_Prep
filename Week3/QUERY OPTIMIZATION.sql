/* QUERY OPTIMIZATION*/
/* it is writing the SQL in a way that reduces unnecessary work for the database*/
/*
SELECT customer_id, amount, order_date
FROM week3_orders
WHERE order_date >= DATE '2024-02-01'
  AND status = 'completed';
  */
  
/* take a SELECT* query and rewrite it with only required columns*/

SELECT 
	customer_id,
    amount,
    order_date
FROM week3_orders WHERE order_date >= '2024-02-01';

/* filtering before aggregation reduces the number of rows processed and ensures that only relevant data is included, improves both accuracy and performance*/

SELECT 
    customer_id,
    SUM(amount) AS total_revenue
FROM week3_orders
WHERE status = 'completed'
  AND order_date >= '2024-02-01'
GROUP BY customer_id;