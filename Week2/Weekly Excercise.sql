/* REtrice all customers*/
SELECT * from customers;

/* Filter customer by city*/
Select * from customers where city = 'chennai'

/* Join tables and display name + amount*/
Select c.name, o.amount FROM customers c
Join orders o ON c.id = o.customer_id;

/* Finding customers with missing values*/
select * from customers where age IS NULL