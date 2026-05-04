/* INDEXES */
/* indexes help the database to find the rows faster, similar to how a book has a index that helps the reader*/
/* the execution plan shows how the database plans to run a query. It can reveal scans, joins, sorts and expensive steps*/
SELECT *
FROM week3_orders
WHERE order_date >= '2024-01-01';