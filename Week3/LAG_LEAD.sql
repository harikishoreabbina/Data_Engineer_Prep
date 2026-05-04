/*LAG helps to compare the current row with previous row.*/

SELECT order_id,customer_id,amount,status,
	lag(amount) over(
		partition by customer_id
		order by order_date) AS previous_order_amount
FROM week3_orders;

/* LEAD helps to compare the current row with the future row*/

SELECT order_id, customer_id, order_date, amount, status,
	lead(order_date) over(
		partition by customer_id
        order by order_date) AS next_order_date
FROM week3_orders;

/* IF THEIR IS NO "ORDER BY" THE THE DATABSE WILL CONFUSE which one is the previous or next one*/
/* we can only use this if we arrange them in a order*/