/* CTE (Common Table Expressions)
it is a Temporary named result created inside a SQL query using WITH
it will not permanently create a table. it only exists while that query runs*/

WITH filtered_customers AS (
	SELECT customer_id,name,city,age
    FROM week3_customers
    WHERE age > 25
)
SELECT * FROM filtered_customers;


WITH completed_orders AS (
	SELECT *
    FROM week3_orders
    WHERE status = 'completed'
)
SELECT * FROM completed_orders


WITH after_orders AS (
	SELECT *
    FROM week3_orders
    WHERE order_date > '2024-02-01'
)
select * FROM after_orders
