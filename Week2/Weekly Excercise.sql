/* REtrice all customers*/
SELECT * from customers;

/* Filter customer by city*/
Select * from customers where city = 'chennai';

/* Join tables and display name + amount*/
select c.name, o.amount FROM customers c
Join orders o ON c.id = o.customer_id;

/*Calculate total orders per customer*/
select c.name, COUNT(o.order_id) AS total_orders
FROM customers c LEFT JOIN orders o 
ON c.id = o.customer_id
GROUP BY c.name;

/* Finding customers with missing values*/
select * from customers where age IS NULL;