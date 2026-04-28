/* GROUP BY is used to GROUP ROWS and apply aggrigations like SUM(), MIN(), MAX(), AVG()*/
SELECT city, count(*) FROM customers GROUP BY city

/*Sum Amounts*/
SELECT customer_id, sum(amount) FROM orders
GROUP BY customer_id;